# Opening network connections - Section introduction and initial examples

### Opening network connections

```text
async loop.create_connection(protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, happy_eyeballs_delay=None, interleave=None, all_errors=False)
```

Open a streaming transport connection to a given address designated by *host* and *port*.

Depending on *host* (or on the *family* argument when one is supplied), the socket family is either [`AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET) or [`AF_INET6`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET6).

The socket type will be [`SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM).

*protocol_factory* must be a callable returning an [asyncio protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

The connection is attempted by this method in the background. On success, it hands back a `(transport, protocol)` pair.

What follows is the step-by-step outline of the operation underneath:

1.

The connection is established and a [transport](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-transport) is created for it.

2.

*protocol_factory* is invoked with no arguments and should return a [protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) instance.

3.

By calling its [`connection_made()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_made) method, the protocol instance is paired with the transport.

4.

A `(transport, protocol)` tuple is returned on success.

The transport that gets created is a bidirectional stream whose details depend on the implementation.

Other arguments:

- *ssl*: when supplied and truthy, an SSL/TLS transport is created (otherwise the default is a plain TCP transport). When *ssl* is an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object, that context builds the transport; when *ssl* is [`True`](https://docs.python.org/3.14/library/constants.html#True), the default context from [`ssl.create_default_context()`](https://docs.python.org/3.14/library/ssl.html#ssl.create_default_context) is applied.

See also

[SSL/TLS security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security)

- *server_hostname* sets or overrides the hostname checked against the target server’s certificate. Pass it only when *ssl* is not `None`. Absent an explicit value, the *host* argument is used by default. When *host* is empty there is no default, so you must provide a *server_hostname*. Supplying an empty string for *server_hostname* turns off hostname matching (a grave security hazard that opens the door to man-in-the-middle attacks).

- For resolving *host*, the optional *family*, *proto*, and *flags* hold the address family, protocol, and flags forwarded into getaddrinfo(). When provided, each must be an integer drawn from the matching [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module constants.

- *happy_eyeballs_delay*, when supplied, switches on Happy Eyeballs for the connection. Give it a floating-point number standing for how many seconds to wait on a connection attempt to finish before launching the next attempt alongside it. That value is the “Connection Attempt Delay” described in [**RFC 8305**](https://datatracker.ietf.org/doc/html/rfc8305.html). The RFC suggests a reasonable default of `0.25` (250 milliseconds).

- *interleave* governs how addresses are reordered when one host name resolves to several IP addresses. With `0` or no value, nothing is reordered and addresses are attempted in the sequence `getaddrinfo()` returns. With a positive integer, addresses get interleaved by address family and that integer stands for the “First Address Family Count” described in [**RFC 8305**](https://datatracker.ietf.org/doc/html/rfc8305.html). It defaults to `0` when *happy_eyeballs_delay* is absent and `1` when it is present.

- *sock*, when supplied, should be an existing, already connected [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) object for the transport to use. When *sock* is supplied, you should leave out *host*, *port*, *family*, *proto*, *flags*, *happy_eyeballs_delay*, *interleave* and *local_addr*.

Note

Passing the *sock* argument hands ownership of the socket over to the transport that gets created. Call the transport’s [`close()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.close) method to close the socket.

- *local_addr*, when supplied, is a `(local_host, local_port)` tuple for binding the socket on the local side. Like *host* and *port*, the *local_host* and *local_port* are resolved through `getaddrinfo()`.

- *ssl_handshake_timeout* is (for a TLS connection) how many seconds to wait on the TLS handshake to finish before giving up on the connection. It is `60.0` seconds when `None` (default).

- *ssl_shutdown_timeout* is how many seconds to wait on the SSL shutdown to finish before giving up on the connection. It is `30.0` seconds when `None` (default).

-

[Subject index](INDEX.md) · [Previous](loop-create-future-to-loop-get-task-factory.md) · [Continue](connection-error-aggregation.md)
