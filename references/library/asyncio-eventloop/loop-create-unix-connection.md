# asyncio.eventloop: `loop.create_unix_connection()`

*reuse_port* instructs the kernel to permit binding this endpoint to a port already held by other existing endpoints, provided every one of them sets this flag at creation time. Windows and several Unix variants lack support for this option. Should the [socket.SO_REUSEPORT](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) constant be undefined, the capability is unavailable.

- *allow_broadcast* instructs the kernel to permit this endpoint to dispatch messages toward the broadcast address.

- *sock* may be supplied optionally so that an existing, already connected [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) object serves the transport. When given, leave out *local_addr* and *remote_addr* (they must be [`None`](https://docs.python.org/3.14/library/constants.html#None)).

Note

The *sock* argument hands the socket's ownership over to the transport that gets created. Closing the socket is done by invoking the transport's [`close()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.close) method.

Refer to the [UDP echo client protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-udp-echo-client-protocol) and [UDP echo server protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-udp-echo-server-protocol) examples.

Changed in version 3.4.4: gained the *family*, *proto*, *flags*, *reuse_address*, *reuse_port*, *allow_broadcast*, plus *sock* parameters.

Changed in version 3.8: Windows became supported.

Changed in version 3.8.1: support for the *reuse_address* parameter was dropped, because relying on [socket.SO_REUSEADDR](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) raises a serious UDP security worry. An exception results from explicitly passing `reuse_address=True`.

Should several processes carrying distinct UIDs bind sockets to one shared UDP socket address using `SO_REUSEADDR`, arriving packets may end up scattered arbitrarily across those sockets.

On platforms where it works, *reuse_port* serves as a substitute offering comparable behavior. The *reuse_port* path relies on [socket.SO_REUSEPORT](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) instead, which expressly blocks processes holding different UIDs from binding sockets to one common socket address.

Changed in version 3.11: the *reuse_address* parameter, switched off back in Python 3.8.1, 3.7.6 and 3.6.10, is now gone completely.

 *async *loop.create_unix_connection(*protocol_factory*, *path=None*, ***, *ssl=None*, *sock=None*, *server_hostname=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*)

Create a Unix connection.

The socket family will be [`AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX); socket type will be [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM).

On success a `(transport, protocol)` tuple comes back.

*path* gives the Unix domain socket's name and must be provided, except when a *sock* parameter is given. Support extends to abstract Unix sockets along with [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) paths.

Consult the documentation for the `loop.create_connection()` method to learn about this method's arguments.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.7: the *ssl_handshake_timeout* parameter arrived. A [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) is now accepted for the *path* parameter.

Changed in version 3.11: the *ssl_shutdown_timeout* parameter arrived.

[Subject index](INDEX.md) · [Continue](loop-create-server.md) · [Owning module, declaration or section: Opening network connections](network-connection-overview.md) · [Owning module, declaration or section: loop.create_datagram_endpoint](loop-create-datagram-endpoint.md) · [Preceding source contract and version conditions](loop-create-datagram-endpoint.md)
