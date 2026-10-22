# socket — Example — Section introduction and initial examples

### Example

What follows are four bare-bones example programs built on the TCP/IP protocol: a server that bounces back every piece of data it receives (handling just one client), plus a client that talks to it. Observe that a server has to run through the sequence `socket()`, `bind()`, `listen()`, `accept()` (perhaps looping the `accept()` to handle several clients), whereas a client needs only the sequence `socket()`, `connect()`. Observe too that the server doesn't call `sendall()`/`recv()` on the socket it listens on, but rather on the fresh socket that `accept()` returns.

Those first two examples handle IPv4 only.

```python
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)

```

```python
# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

```

The two examples coming up match the previous pair, except they handle IPv4 and IPv6 alike. On the server side, it listens to the first address family on offer (ideally it would listen to both). Across most IPv6-ready systems, IPv6 wins out and the server may turn away IPv4 traffic. On the client side, it attempts each address that name resolution yields and routes traffic to whichever one connects first.

```python
# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)

```

[Subject index](INDEX.md) · [Previous](timeouts-and-the-accept-method.md) · [Continue](example-code-example-import-socket-continue-to-break.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
