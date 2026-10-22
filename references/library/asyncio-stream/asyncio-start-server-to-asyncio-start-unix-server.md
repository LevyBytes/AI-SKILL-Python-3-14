# Streams: `asyncio.start_server()`, `asyncio.open_unix_connection()`, `asyncio.start_unix_server()`

`*async *asyncio.start_server(*client_connected_cb*, *host=None*, *port=None*, ***, *limit=None*, *family=socket.AF_UNSPEC*, *flags=socket.AI_PASSIVE*, *sock=None*, *backlog=100*, *ssl=None*, *reuse_address=None*, *reuse_port=None*, *keep_alive=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*, *start_serving=True*)`

Bring up a socket server.

Each time a fresh client connection comes in, the *client_connected_cb* callback fires. It is handed a `(reader, writer)` pair as its two arguments — instances of the `StreamReader` and `StreamWriter` classes.

*client_connected_cb* may be an ordinary callable or a [coroutine function](https://docs.python.org/3.14/library/asyncio-task.html#coroutine); when it is a coroutine function, it gets scheduled automatically as a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).

The buffer size cap applied by the returned `StreamReader` instance is set by *limit*. Absent any value, that *limit* defaults to 64 KiB.

Every remaining argument is forwarded as-is to [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server).

Note

Supplying the *sock* argument moves ownership of the socket onto the server that gets created. To shut the socket, invoke the server's [`close()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.close) method.

Changed in version 3.7: Added the *ssl_handshake_timeout* and *start_serving* parameters.

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Added the *ssl_shutdown_timeout* parameter.

Changed in version 3.13: Added the *keep_alive* parameter.

Unix Sockets

 `*async *asyncio.open_unix_connection(*path=None*, ***, *limit=None*, *ssl=None*, *sock=None*, *server_hostname=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*)`

Open a Unix socket connection and give back a `(reader, writer)` pair.

This mirrors `open_connection()` while acting on Unix sockets instead.

Have a look as well at the documentation for [`loop.create_unix_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection).

Note

Handing in the *sock* argument transfers the socket's ownership to the `StreamWriter` that is created. Shut the socket by calling its `close()` method.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.7: Added the *ssl_handshake_timeout* parameter. From here on, a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) is acceptable for the *path* parameter

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Added the *ssl_shutdown_timeout* parameter.

 `*async *asyncio.start_unix_server(*client_connected_cb*, *path=None*, ***, *limit=None*, *sock=None*, *backlog=100*, *ssl=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*, *start_serving=True*, *cleanup_socket=True*)`

Bring up a Unix socket server.

This mirrors `start_server()` while functioning with Unix sockets.

When *cleanup_socket* is true, the Unix socket is taken off the filesystem on its own once the server closes — unless the socket got swapped out after the server was created.

Have a look as well at the documentation for [`loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server).

Note

With the *sock* argument given, ownership of the socket moves to the server that is created. Close the socket by invoking the server's [`close()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.close) method.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.7: Added the *ssl_handshake_timeout* and *start_serving* parameters. The *path* parameter henceforth accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Added the *ssl_shutdown_timeout* parameter.

Changed in version 3.13: Added the *cleanup_socket* parameter.

[Subject index](INDEX.md) · [Previous](asyncio-open-connection.md) · [Continue](asyncio-streamreader-class.md) · [Owning module, declaration or section: Streams](asyncio-open-connection.md)
