<h2 align="center">Client Side Programming</h2>
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

## use connection object, in order to send information
## do it in form of bytes through typecasting b"message"
connection.send(b"Hello there!")
```
---
> [payload.py](payload.py)
```python
import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

## write code to receive and decode message
output = payload.recv(2048) # 1024 is approximately 1K bytes, 2048 is 2K bytes of data
## convert output in a form of string
print(output.decode("utf-8"))
```