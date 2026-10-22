# Python 3.12.0 alpha 1 / library / socket

[gh-96388](https://github.com/python/cpython/issues/96388): Absent socket functions are worked around inside the `__repr__` of [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket).

[gh-91968](https://github.com/python/cpython/issues/91968): Bring the `SO_RTABLE` and `SO_USER_COOKIE` constants into [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket).

[gh-94821](https://github.com/python/cpython/issues/94821): Binding a unix socket to an empty address on Linux now grabs a free address out of the abstract namespace rather than “0”.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
