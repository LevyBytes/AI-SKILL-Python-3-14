# asyncio.eventloop: `loop.sock_recv()`, `loop.sock_recv_into()`, `loop.sock_recvfrom()`, `loop.sock_recvfrom_into()`, `loop.sock_sendall()`, `loop.sock_sendto()`, `loop.sock_connect()`

### Working with socket objects directly

Broadly speaking, protocol implementations built on transport-based APIs like `loop.create_connection()` and `loop.create_server()` run faster than those operating on sockets directly. Even so, certain scenarios put little weight on performance, and handling [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) objects directly proves more convenient.

 *async *loop.sock_recv(*sock*, *nbytes*)

Pull as many as *nbytes* off *sock*. Asynchronous version of [`socket.recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv).

Return the received data as a bytes object.

*sock* must be a non-blocking socket.

Changed in version 3.7: although this method had always carried documentation as a coroutine method, releases ahead of Python 3.7 handed back a [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future). From Python 3.7 onward it is an `async def` method.

 *async *loop.sock_recv_into(*sock*, *buf*)

Read data out of *sock* into the *buf* buffer. Patterned on the blocking [`socket.recv_into()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv_into) method.

Return the number of bytes written to the buffer.

*sock* must be a non-blocking socket.

Added in version 3.7.

 *async *loop.sock_recvfrom(*sock*, *bufsize*)

Pull a datagram as large as *bufsize* off *sock*. Asynchronous version of [`socket.recvfrom()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvfrom).

Return a tuple of (received data, remote address).

*sock* must be a non-blocking socket.

Added in version 3.11.

 *async *loop.sock_recvfrom_into(*sock*, *buf*, *nbytes=0*)

Pull a datagram as large as *nbytes* off *sock* into *buf*. Asynchronous version of [`socket.recvfrom_into()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvfrom_into).

Return a tuple of (number of bytes received, remote address).

*sock* must be a non-blocking socket.

Added in version 3.11.

 *async *loop.sock_sendall(*sock*, *data*)

Send *data* to the *sock* socket. Asynchronous version of [`socket.sendall()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendall).

This method keeps writing to the socket until every byte in *data* has gone out or an error arises. On success `None` comes back. When an error occurs, an exception is raised. Moreover, there is no means of telling how much data, if any, the connection's receiving side actually handled.

*sock* must be a non-blocking socket.

Changed in version 3.7: although the method had always carried documentation as a coroutine method, ahead of Python 3.7 it handed back a [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future). From Python 3.7 onward, it is an `async def` method.

 *async *loop.sock_sendto(*sock*, *data*, *address*)

Send a datagram from *sock* to *address*. Asynchronous version of [`socket.sendto()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendto).

Return the number of bytes sent.

*sock* must be a non-blocking socket.

Added in version 3.11.

 *async *loop.sock_connect(*sock*, *address*)

Connect *sock* to a remote socket at *address*.

Asynchronous version of [`socket.connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect).

*sock* must be a non-blocking socket.

Changed in version 3.5.2: resolving `address` ahead of time is no longer necessary. `sock_connect` attempts to detect whether the *address* already resolved by calling [`socket.inet_pton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_pton). Failing that, `loop.getaddrinfo()` handles resolving the *address*.

See also

`loop.create_connection()` and [`asyncio.open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection).

[Subject index](INDEX.md) · [Previous](loop-add-reader-to-loop-remove-writer.md) · [Continue](loop-sock-accept-to-loop-sock-sendfile.md)
