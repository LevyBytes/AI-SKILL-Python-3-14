# Python 3.14.6 final / library / socket

[gh-150406](https://github.com/python/cpython/issues/150406): Repair a possible segfault that happens during [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module initialization once the system runs out of memory on platforms lacking a reentrant `gethostbyname`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
