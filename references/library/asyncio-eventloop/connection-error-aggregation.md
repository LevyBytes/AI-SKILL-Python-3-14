# Opening network connections - Contract: *all_errors* dictates which exceptions surface when a connection cannot be established.

*all_errors* dictates which exceptions surface when a connection cannot be established. By default a lone `Exception` is raised: the first exception when there is only one or when every error shares the same message, or one `OSError` whose error messages have been merged. With `all_errors` set to `True`, an `ExceptionGroup` carrying every exception is raised (even where just one exists).

Changed in version 3.5: Added support for SSL/TLS in `ProactorEventLoop`.

Changed in version 3.6: For every TCP connection, the [socket.TCP_NODELAY](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) socket option now defaults to being enabled.

Changed in version 3.7: Added the *ssl_handshake_timeout* parameter.

Changed in version 3.8: Added the *happy_eyeballs_delay* and *interleave* parameters.

Happy Eyeballs Algorithm: Success with Dual-Stack Hosts. When the IPv4 path and protocol to a server function but its IPv6 path and protocol do not, a dual-stack client application suffers a noticeable connection delay next to an IPv4-only client. That outcome is undesirable, since it worsens the dual-stack client’s user experience. The present document lays out requirements for algorithms that shrink this user-visible delay and supplies one such algorithm.

For more information: [https://datatracker.ietf.org/doc/html/rfc6555](https://datatracker.ietf.org/doc/html/rfc6555)

Changed in version 3.11: Added the *ssl_shutdown_timeout* parameter.

Changed in version 3.12: *all_errors* was added.

See also

As a high-level alternative API, the [`open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection) function yields a ([`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader), [`StreamWriter`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter)) pair you can drive straight from async/await code.

[Subject index](INDEX.md) · [Previous](network-connection-overview.md) · [Continue](loop-create-datagram-endpoint.md) · [Owning module, declaration or section: Opening network connections](network-connection-overview.md)
