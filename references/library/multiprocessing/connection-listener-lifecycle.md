# multiprocessing / Listeners and Clients: `multiprocessing.connection.Listener`, `accept()`, `close()`

*class *multiprocessing.connection.Listener([*address*[, *family*[, *backlog*[, *authkey*]]]])

A wrapper around a bound socket or Windows named pipe that is ‘listening’ for connections.

*address* is the address the listener object's bound socket or named pipe is to use.

Note

When an address of ‘0.0.0.0’ is used, it will not form a connectable endpoint on Windows. Should you need a connectable endpoint, go with ‘127.0.0.1’.

*family* is the kind of socket (or named pipe) to use. The accepted strings are `'AF_INET'` (a TCP socket), `'AF_UNIX'` (a Unix domain socket) or `'AF_PIPE'` (a Windows named pipe). Of those, availability is guaranteed only for the first. When *family* is `None`, the family is deduced from the layout of *address*. When *address* is `None` as well, a default gets chosen. That default is the family taken to be the fastest available one. See Address Formats. Note that when *family* is `'AF_UNIX'` and address is `None`, the socket is created inside a private temporary directory made with [`tempfile.mkstemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkstemp).

When the listener object uses a socket then *backlog* (1 by default) gets passed to the socket's [`listen()`](https://docs.python.org/3.14/library/socket.html#socket.socket.listen) method once it has been bound.

When *authkey* is supplied and not `None`, it should be a byte string and serves as the secret key for an HMAC-based authentication challenge. No authentication happens when *authkey* is `None`. `AuthenticationError` is raised when authentication fails. See Authentication keys.

 accept()

Accept a connection on the listener object's bound socket or named pipe and give back a `Connection` object. When authentication is tried and it fails, `AuthenticationError` is raised.

 close()

Close the listener object's bound socket or named pipe. This runs automatically once the listener is garbage collected. Even so, calling it explicitly is advisable.

Listener objects have the following read-only properties:

 address

The address the Listener object is using.

 last_accepted

The address that the last accepted connection arrived from. When this is unavailable, it is `None`.

Changed in version 3.3: The context management protocol is now supported by Listener objects – see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) returns the listener object, while [`__exit__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__exit__) calls `close()`.

[Subject index](INDEX.md) · [Previous](connection-authentication-and-client.md) · [Continue](multiprocessing-connection-wait.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Listeners and Clients](connection-authentication-and-client.md)
