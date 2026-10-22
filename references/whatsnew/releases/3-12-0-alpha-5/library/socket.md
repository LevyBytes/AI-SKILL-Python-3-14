# Python 3.12.0 alpha 5 / library / socket

[gh-100795](https://github.com/python/cpython/issues/100795): Head off a possible unexpected `freeaddrinfo` call (double free) within [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) for the case where a libc `getaddrinfo()` implementation leaves junk in an output pointer while returning an error. Sergey G. Brester provided the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
