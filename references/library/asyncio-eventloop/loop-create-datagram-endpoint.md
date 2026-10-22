# asyncio.eventloop: `loop.create_datagram_endpoint()`

*async *loop.create_datagram_endpoint(*protocol_factory*, *local_addr=None*, *remote_addr=None*, ***, *family=0*, *proto=0*, *flags=0*, *reuse_port=None*, *allow_broadcast=None*, *sock=None*)

Create a datagram connection.

Depending on *host* (or on the *family* argument when one is supplied), the socket family is either [`AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET), [`AF_INET6`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET6), or [`AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX).

The socket type will be [`SOCK_DGRAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_DGRAM).

*protocol_factory* must be a callable returning a [protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

A tuple of `(transport, protocol)` is returned on success.

Other arguments:

- *local_addr*, when supplied, is a `(local_host, local_port)` tuple for binding the socket on the local side. The *local_host* and *local_port* are resolved through `getaddrinfo()`.

Note

Running this on Windows under the proactor event loop while `local_addr=None` triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) carrying `errno.WSAEINVAL`.

- *remote_addr*, when supplied, is a `(remote_host, remote_port)` tuple for connecting the socket to a remote address. The *remote_host* and *remote_port* are resolved through `getaddrinfo()`.

- For resolving *host*, the optional *family*, *proto*, and *flags* hold the address family, protocol, and flags forwarded into `getaddrinfo()`. When provided, each must be an integer drawn from the matching [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module constants.

-

[Subject index](INDEX.md) · [Previous](connection-error-aggregation.md) · [Owning module, declaration or section: Opening network connections](network-connection-overview.md) · [Required continuation of the source contract](loop-create-unix-connection.md)
