<h2 align="center">Send message from Server to Client</h2>
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

## create loop that will iterate continuously
while True:
	inp = input(">> ")
	## convert the input string into bytes and decoded
	connection.send(bytes(inp, "utf-8"))
	
	## server machine should also receive information same as client
	recv = connection.recv(2048)
	print(recv.decode("utf-8"))
```
---
> [payload.py](payload.py)
```python
import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

## create loop that will receive data continuously sent by client machine
while True:
	recv = payload.recv(2048)
	print(recv.decode("utf-8"))

	## if the client machine wants to send information first
	inp = input(">> ")
	## convert the input string into bytes and decoded
	payload.send(bytes(inp, "utf-8"))
```