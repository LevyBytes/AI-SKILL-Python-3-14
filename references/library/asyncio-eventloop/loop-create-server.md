# asyncio.eventloop: `loop.create_server()`

### Creating network servers

 *async *loop.create_server(*protocol_factory*, *host=None*, *port=None*, ***, *family=socket.AF_UNSPEC*, *flags=socket.AI_PASSIVE*, *sock=None*, *backlog=100*, *ssl=None*, *reuse_address=None*, *reuse_port=None*, *keep_alive=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*, *start_serving=True*)

Stand up a TCP server (socket type [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM)) that listens on the *host* address's *port*.

Returns a `Server` object.

Arguments:

- *protocol_factory* must be a callable returning a [protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

- Several types may be assigned to the *host* parameter, each dictating where the server will listen:

  - When *host* holds a string, the TCP server binds to one network interface named by *host*.

  - When *host* holds a sequence of strings, the TCP server binds to every network interface that the sequence names.

  - When *host* is an empty string or `None`, every interface is assumed and a list containing several sockets gets returned (typically one for IPv4 plus another for IPv6).

- Use the *port* parameter to indicate the port on which the server ought to listen. When it is `0` or `None` (the default), an unused port chosen at random is selected (be aware that if *host* maps to several network interfaces, each interface gets its own randomly chosen port).

- Setting *family* to [`socket.AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET) or [`AF_INET6`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET6) compels the socket toward IPv4 or IPv6 respectively. Leaving it unset derives the *family* from the host name (the default being [`AF_UNSPEC`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNSPEC)).

- *flags* is a bitmask for `getaddrinfo()`.

- *sock* may be supplied optionally so that an existing socket object is used. When it is given, omit both *host* and *port*.

Note

The *sock* argument hands the socket's ownership over to the server that gets created. Closing the socket is done by invoking the server's `close()` method.

- *backlog* sets the ceiling on queued connections forwarded to [`listen()`](https://docs.python.org/3.14/library/socket.html#socket.socket.listen) (the default being 100).

- Supplying *ssl* an [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance turns on TLS across the connections that are accepted.

- *reuse_address* directs the kernel to reuse a local socket sitting in `TIME_WAIT` state rather than waiting out its normal timeout. When left unspecified, it defaults to `True` automatically on Unix.

- *reuse_port* instructs the kernel to permit binding this endpoint to a port already held by other existing endpoints, provided every one of them sets this flag at creation time. Windows lacks support for this option.

- Giving *keep_alive* the value `True` holds connections open by switching on the regular sending of messages.

Changed in version 3.13: the *keep_alive* parameter arrived.

- *ssl_handshake_timeout* sets, for a TLS server, how many seconds to await completion of the TLS handshake before the connection is aborted. It is `60.0` seconds when `None` (the default).

- *ssl_shutdown_timeout* sets how many seconds to await completion of the SSL shutdown before the connection is aborted. It is `30.0` seconds when `None` (the default).

- Giving *start_serving* the value `True` (the default) has the new server begin accepting connections right away. With `False`, the user should await `Server.start_serving()` or `Server.serve_forever()` so the server starts taking connections.

Changed in version 3.5: SSL/TLS gained support within `ProactorEventLoop`.

Changed in version 3.5.1: a sequence of strings became permissible for the *host* parameter.

Changed in version 3.6: the *ssl_handshake_timeout* and *start_serving* parameters arrived. By default the socket option [socket.TCP_NODELAY](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) is applied to every TCP connection.

Changed in version 3.11: the *ssl_shutdown_timeout* parameter arrived.

See also

The [`start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server) function offers a higher-level alternative API yielding a pair, [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) and [`StreamWriter`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter), usable from async/await code.

[Subject index](INDEX.md) · [Continue](loop-create-unix-server-to-loop-connect-accepted-socket.md)
