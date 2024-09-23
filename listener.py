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
