# Python 3.12.0 alpha 1 / build / socket

[gh-95174](https://github.com/python/cpython/issues/95174): Under WASI, Python now bypasses missing [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) functions and methods. WASI is only able to build sockets out of an existing fd / accept and provides no netdb.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
