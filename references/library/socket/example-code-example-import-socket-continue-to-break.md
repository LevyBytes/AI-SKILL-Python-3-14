# socket: Windows packet capture and CAN socket examples

```python
# Echo client program
import socket
import sys

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

```

The example that follows demonstrates building a very basic network sniffer out of raw sockets on Windows. Running it calls for administrator privileges so the interface can be altered:

```python
import socket

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packets
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a packet
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

```

The example that follows demonstrates driving the socket interface to talk to a CAN network over the raw socket protocol. Should you instead want CAN with the broadcast manager protocol, open a socket like so:

```python
socket.socket(socket.AF_CAN, socket.SOCK_DGRAM, socket.CAN_BCM)

```

Once the socket has been bound (`CAN_RAW`) or connected (`CAN_BCM`), the `socket.send()` and `socket.recv()` operations (along with their counterparts) work on the socket object just as they normally would.

Running this final example may well call for special privileges:

[Subject index](INDEX.md) · [Previous](example-section-introduction-and-initial-examples.md) · [Continue](can-frame-encoding-and-decoding-example.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Example](example-section-introduction-and-initial-examples.md)
