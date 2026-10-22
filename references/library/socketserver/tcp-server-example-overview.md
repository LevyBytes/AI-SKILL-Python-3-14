# socketserver — `socketserver.TCPServer` Example — Section introduction and initial examples

### Examples

### `socketserver.TCPServer` Example

This is the server side:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)
        print(f"Received from {self.client_address[0]}:")
        print(self.data.decode("utf-8"))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        # after we return, the socket will be closed.

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

```

A different request handler class built on streams — file-like objects that ease communication by exposing the standard file interface:

```python
class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler.
        # We can now use e.g. readline() instead of raw recv() calls.
        # We limit ourselves to 10000 bytes to avoid abuse by the sender.
        self.data = self.rfile.readline(10000).rstrip()
        print(f"{self.client_address[0]} wrote:")
        print(self.data.decode("utf-8"))
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())

```

Here the distinction is that the second handler's `readline()` call keeps invoking `recv()` until a newline character turns up, whereas the first handler needed a `recv()` loop to gather data right up to a newline on its own. Had it relied on one lone `recv()` with no loop, it would simply have returned whatever had been received from the client up to that point. TCP works on streams: data comes through in the same order it left, yet there is no link between a client's `send()` or `sendall()` calls and how many `recv()` calls the server needs to take it all in.

This is the client side:

[Subject index](INDEX.md) · [Continue](socketserver-tcpserver-example-code-example-import-socket.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)
