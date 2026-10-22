# DNS

### DNS

 *async *loop.getaddrinfo(*host*, *port*, ***, *family=0*, *type=0*, *proto=0*, *flags=0*)

Asynchronous version of [`socket.getaddrinfo()`](https://docs.python.org/3.14/library/socket.html#socket.getaddrinfo).

 *async *loop.getnameinfo(*sockaddr*, *flags=0*)

Asynchronous version of [`socket.getnameinfo()`](https://docs.python.org/3.14/library/socket.html#socket.getnameinfo).

Note

Internally, both *getaddrinfo* and *getnameinfo* run their synchronous counterparts via the loop's default thread pool executor. Once that executor becomes saturated, these methods can incur delays that higher-level networking libraries may surface as elevated timeouts. As a remedy, think about dedicating a custom executor to your other tasks, or registering a default executor backed by a greater worker count.

Changed in version 3.7: the *getaddrinfo* and *getnameinfo* methods were each always documented as returning a coroutine, yet before Python 3.7 they actually returned [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) objects. Beginning with Python 3.7 both methods are coroutines.

[Subject index](INDEX.md) · [Previous](loop-sock-accept-to-loop-sock-sendfile.md) · [Continue](loop-connect-read-pipe-to-loop-connect-write-pipe.md)
