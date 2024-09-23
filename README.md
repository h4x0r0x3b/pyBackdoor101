<h2 align="center">Python Backdoor 101</h2>
<p align="center"><img width="350" height="350" src="./src/banner_cnph.gif"></p>

- - - - - - - - - - - - - - - - - - - - - -
#### Domain

is the family of protocols that is used as the transport mechanism. These values are constants such as **AF_INET**, **AF_UNIX**, PF_INET, PF_UNIX, PF_X25, and so on.

#### Type

means the kind of communication between two endpoints, typically **SOCK_STREAM** for connection-oriented protocols and **SOCK_DGRAM** for connectionless protocols.

#### Protocol

This may be used to identify a variant of a protocol within a domain and type. Its default value is **0**. This is usually left out.

#### Hostname

This works as the identifier of a network interface. A hostname nay be a string, a dotted-quad address, or an IPV6 address in colon (and possibly dot) notation.

#### Port

Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string containing a port number, or the name of a service.

use the Socket module to implement socket programming in python,<br>
import the socket library and then make a simple socket.
```python
import socket
s = socket.socket (socket_family, socket_type, protocol = 0)
```
- **socket_family** − This is either **AF_UNIX** or  **AF_INET**
- **socket_type** − This is either **SOCK_STREAM** or **SOCK_DGRAM**
- **protocol** − This is usually left out, defaulting to **0**.

---
<h3 align="center">The three different set of socket methods :</h2>

- [Server Socket Methods](#server-socket-method)
- [Client Socket Methods](#client-socket-methods)
- [General Socket Methods](#general-socket-methods)

---

#### Server Socket Methods

In the client-server architecture, there is one centralized server that provides service and
many clients receive service from that centralized server.

The clients also do the request
to server.

A few important server socket methods in this architecture are as follows:

- **socket.bind()** : This method binds the address (hostname, port number) to the socket.

- **socket.listen()** : This method basically listens to the connections made to the socket. It starts TCP listener. Backlog is an argument of this method which specifies the maximum number of queued connections. Its minimum value is 0 and maximum value is 5.

- **socket.accept()** : This will accept TCP client connection. The pair (conn, address) is the return value pair of this method. Here, conn is a new socket object used to send and receive data on the connection and address is the address bound to the socket. Before using this method, the socket.bind() and socket.listen() method must be used.

---

#### Client Socket Methods

The client in the client-server architecture requests the server and receives services from
the server. For this, there is only one method dedicated for clients:

- **socket.connect(address)** : this method actively intimate server connection or in simple words this method connects the client to the server. The argument address represents the address of the server.

---

#### General Socket Methods

Other than client and server socket methods, there are some general socket methods, which are very useful in socket programming.

The general socket methods are as follows:

- **socket.recv(bufsize)** : As name implies, this method receives the TCP message from socket. The argument bufsize stands for buffer size and defines the maximum data this method can receive at any one time.

- **socket.send(bytes)** : This method is used to send data to the socket which is connected to the remote machine. The argument bytes will gives the number of bytes sent to the socket.

- **socket.recvfrom(data, address)** : This method receives data from the socket. Two pair (data, address) value is returned by this method. Data defines the received data and address specifies the address of socket sending the data.

- **socket.sendto(data, address)** : As name implies, this method is used to send data from the socket. Two pair (data, address) value is returned by this method. Data defines the number of bytes sent and address specifies the address of the
remote machine.

- **socket.close()** : This method will close the socket.

- **socket.gethostname()** : This method will return the name of the host.

- **socket.sendall(data)** : This method sends all the data to the socket which is connected to a remote machine. It will carelessly transfers the data until an error occurs and if it happens then it uses socket.close() method to close the socket.