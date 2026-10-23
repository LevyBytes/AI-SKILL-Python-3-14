# socketserver`socketserver.TCPServer` Example - Code example: import socket

```python
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, "utf-8"))
    sock.sendall(b"\n")

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:    ", data)
print("Received:", received)

```

Running the example should give you output along these lines:

Server:

```shell
$ python TCPServer.py
127.0.0.1 wrote:
b'hello world with TCP'
127.0.0.1 wrote:
b'python is nice'

```

Client:

```shell
$ python TCPClient.py hello world with TCP
Sent:     hello world with TCP
Received: HELLO WORLD WITH TCP
$ python TCPClient.py python is nice
Sent:     python is nice
Received: PYTHON IS NICE

```

[Subject index](INDEX.md) · [Previous](tcp-server-example-overview.md) · [Continue](socketserver-udpserver-example.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: `socketserver.TCPServer` Example](tcp-server-example-overview.md)
