## use socket library
import socket

## create listener object module of socket and specify 2 constant
## socket.AF_INET specifies the (AF) Address Family (INET) Internet address for IPv4
## socket.SOCK_STREAM is the socket type for TCP communication
## TCP is a protocol used to transport messages in the network
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Binds the address (hostname, port number) to the socket
## Bind the listener with 2 arguments in a Tuple (similar to lists)
## 1st argument is the hostname/IP address of the server machine
## If you want to implement attack over the internet/web, use public IP address
## 2nd argument is the open port of the server machine
listener.bind(("attacker_ip", 1337))

## listen to any incoming communication (server side)
## use the same object created and call the listen method
listener.listen()
