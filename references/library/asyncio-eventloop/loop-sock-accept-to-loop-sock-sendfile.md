# asyncio.eventloop: `loop.sock_accept()`, `loop.sock_sendfile()`

*async *loop.sock_accept(*sock*)

Accept a connection. Patterned on the blocking [`socket.accept()`](https://docs.python.org/3.14/library/socket.html#socket.socket.accept) method.

The socket has to be bound to an address and listening for connections. What gets returned is a pair `(conn, address)` in which *conn* is a *new* socket object suitable for sending and receiving data over the connection, while *address* is the address bound to the socket at the connection's far end.

*sock* must be a non-blocking socket.

Changed in version 3.7: although the method had always carried documentation as a coroutine method, ahead of Python 3.7 it handed back a [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future). From Python 3.7 onward, it is an `async def` method.

See also

`loop.create_server()` and [`start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server).

 *async *loop.sock_sendfile(*sock*, *file*, *offset=0*, *count=None*, ***, *fallback=True*)

Transmit a file via high-performance [`os.sendfile`](https://docs.python.org/3.14/library/os.html#os.sendfile) where feasible. Return the total number of bytes sent.

Asynchronous version of [`socket.sendfile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendfile).

*sock* must be a non-blocking [`socket.SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM) [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket).

*file* must be a regular file object open in binary mode.

*offset* indicates the point from which file reading begins. When supplied, *count* is the overall byte count to send, rather than transmitting the file all the way to EOF. The file position always advances, even if this method raises an error, and [`file.tell()`](https://docs.python.org/3.14/library/io.html#io.IOBase.tell) serves to retrieve the true count of bytes sent.

Giving *fallback* the value `True` lets asyncio read and send the file by hand wherever the platform offers no sendfile syscall (for instance Windows, or an SSL socket on Unix).

Raise [`SendfileNotAvailableError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError) where the *sendfile* syscall is unsupported by the system and *fallback* holds `False`.

*sock* must be a non-blocking socket.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](loop-sock-recv-to-loop-sock-connect.md) · [Continue](loop-getaddrinfo-to-loop-getnameinfo.md) · [Owning module, declaration or section: Working with socket objects directly](loop-sock-recv-to-loop-sock-connect.md)
