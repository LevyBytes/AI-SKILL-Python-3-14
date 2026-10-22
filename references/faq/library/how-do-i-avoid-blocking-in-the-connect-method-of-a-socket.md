# How do I avoid blocking in the connect() method of a socket?

### How do I avoid blocking in the connect() method of a socket?

To help with asynchronous I/O on sockets, the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module is the one commonly turned to.

So that the TCP connect doesn't stall, switch the socket into non-blocking mode. With that done, calling [`connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect) will either succeed right away (rarely) or raise an exception whose error code sits in `.errno`. A value of `errno.EINPROGRESS` means the connection has begun but is not yet complete. Because each operating system reports its own values here, you'll need to inspect whatever your particular platform hands back.

To sidestep raising an exception altogether, reach for the [`connect_ex()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect_ex) method, which simply hands back the errno value. For polling, invoke `connect_ex()` once more a bit later – a result of `0` or `errno.EISCONN` tells you the link is established – or feed the socket into [`select.select()`](https://docs.python.org/3.14/library/select.html#select.select) to test whether it has become writable.

Note

The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module is a general-purpose, single-threaded, concurrent asynchronous library well suited to authoring non-blocking networking code. Outside the standard library, the well-liked and richly featured [Twisted](https://twisted.org/) library offers another option.

[Subject index](INDEX.md)
