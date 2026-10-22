# ssl — Server-side operation

### Server-side operation

To operate as a server, you will generally require a server certificate plus a private key, each held in a file. First you create a context that carries the key and the certificate, allowing clients to confirm that you are genuine. Next you open a socket, bind it to a port, invoke `listen()` on it, and begin awaiting client connections:

```python
import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="mycertfile", keyfile="mykeyfile")

bindsocket = socket.socket()
bindsocket.bind(('myaddr.example.com', 10023))
bindsocket.listen(5)

```

After a client connects, you invoke `accept()` on the socket to obtain the new socket coming from the far end, then apply the context's `SSLContext.wrap_socket()` method to produce a server-side SSL socket for that connection:

```python
while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

```

From there you read data off the `connstream` and act on it until you have wrapped up with the client (or the client has wrapped up with you):

```python
def deal_with_client(connstream):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.recv(1024)
    # finished with client

```

Then you resume listening for fresh client connections (naturally, an actual server would likely service each client connection in its own thread, or set the sockets to non-blocking mode and rely on an event loop).

[Subject index](INDEX.md) · [Previous](tls-client-http-request.md) · [Continue](notes-on-non-blocking-sockets.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
