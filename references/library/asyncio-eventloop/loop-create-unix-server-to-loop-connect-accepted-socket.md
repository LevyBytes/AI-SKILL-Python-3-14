# asyncio.eventloop: `loop.create_unix_server()`, `loop.connect_accepted_socket()`

*async *loop.create_unix_server(*protocol_factory*, *path=None*, ***, *sock=None*, *backlog=100*, *ssl=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*, *start_serving=True*, *cleanup_socket=True*)

Resembles `loop.create_server()` yet operates over the [`AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX) socket family.

*path* gives the Unix domain socket's name and must be provided, except when a *sock* argument is supplied. Support extends to abstract Unix sockets along with [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) paths.

When *cleanup_socket* is true, the Unix socket gets deleted from the filesystem automatically once the server closes, except where the socket was swapped out after the server's creation.

Consult the documentation for the `loop.create_server()` method to learn about this method's arguments.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.7: the *ssl_handshake_timeout* and *start_serving* parameters arrived. A [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) object is now accepted for the *path* parameter.

Changed in version 3.11: the *ssl_shutdown_timeout* parameter arrived.

Changed in version 3.13: the *cleanup_socket* parameter arrived.

 *async *loop.connect_accepted_socket(*protocol_factory*, *sock*, ***, *ssl=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*)

Wrap an already accepted connection into a transport/protocol pair.

Servers that accept their connections outside asyncio yet rely on asyncio to process them can employ this method.

Parameters:

- *protocol_factory* must be a callable returning a [protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

- *sock* is an existing socket object handed back from [`socket.accept`](https://docs.python.org/3.14/library/socket.html#socket.socket.accept).

Note

The *sock* argument hands the socket's ownership over to the transport that gets created. Closing the socket is done by invoking the transport's [`close()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.close) method.

- Supplying *ssl* an [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) turns on SSL across the connections that are accepted.

- *ssl_handshake_timeout* sets, for an SSL connection, how many seconds to await completion of the SSL handshake before the connection is aborted. It is `60.0` seconds when `None` (the default).

- *ssl_shutdown_timeout* sets how many seconds to await completion of the SSL shutdown before the connection is aborted. It is `30.0` seconds when `None` (the default).

Returns a `(transport, protocol)` pair.

Added in version 3.5.3.

Changed in version 3.7: the *ssl_handshake_timeout* parameter arrived.

Changed in version 3.11: the *ssl_shutdown_timeout* parameter arrived.

[Subject index](INDEX.md) · [Previous](loop-create-server.md) · [Continue](loop-sendfile.md) · [Owning module, declaration or section: Creating network servers](loop-create-server.md)
