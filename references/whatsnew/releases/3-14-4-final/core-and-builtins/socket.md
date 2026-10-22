# Python 3.14.4 final / core and builtins / socket

[gh-146245](https://github.com/python/cpython/issues/146245): Resolved reference leaks within [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) that appeared when audit hooks throw exceptions during [`socket.getaddrinfo()`](https://docs.python.org/3.14/library/socket.html#socket.getaddrinfo) and `socket.sendto()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
