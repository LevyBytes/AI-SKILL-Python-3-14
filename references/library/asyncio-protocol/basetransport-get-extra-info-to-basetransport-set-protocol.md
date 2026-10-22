# asyncio.protocol: `BaseTransport.get_extra_info()`, `BaseTransport.set_protocol()`

BaseTransport.get_extra_info(*name*, *default=None*)

Return information about the transport or underlying resources it uses.

*name* is a string naming which transport-specific detail you want retrieved.

*default* is the value handed back when the information isn't available, or when the transport can't be queried for it on the current platform or under the given third-party event loop implementation.

As an illustration, the snippet below tries to retrieve the transport's underlying socket object:

```python
sock = transport.get_extra_info('socket')
if sock is not None:
    print(sock.getsockopt(...))

```

Kinds of information that certain transports let you query:

- socket:

  - `'peername'`: the remote endpoint the socket has connected to, as returned by [`socket.socket.getpeername()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getpeername) (`None` on error)

  - `'socket'`: [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) instance

  - `'sockname'`: the socket's own address, result of [`socket.socket.getsockname()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockname)

- SSL socket:

  - `'compression'`: the active compression algorithm given as a string, or `None` when no compression applies to the connection; as returned by [`ssl.SSLSocket.compression()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.compression)

  - `'cipher'`: a tuple of three values holding the active cipher's name, the SSL protocol version that specifies its usage, and the count of secret bits in play; as returned by [`ssl.SSLSocket.cipher()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.cipher)

  - `'peercert'`: peer certificate; result of [`ssl.SSLSocket.getpeercert()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.getpeercert)

  - `'sslcontext'`: [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance

  - `'ssl_object'`: [`ssl.SSLObject`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLObject) or [`ssl.SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) instance

- pipe:

  - `'pipe'`: pipe object

- subprocess:

  - `'subprocess'`: [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) instance

 BaseTransport.set_protocol(*protocol*)

Set a new protocol.

Only swap protocols in cases where each protocol is documented as supporting the switch.

[Subject index](INDEX.md) · [Previous](basetransport-close-to-basetransport-is-closing.md) · [Continue](basetransport-get-protocol.md) · [Owning module, declaration or section: Base Transport](basetransport-close-to-basetransport-is-closing.md)
