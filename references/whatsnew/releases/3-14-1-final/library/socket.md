# Python 3.14.1 final / library / socket

[gh-100218](https://github.com/python/cpython/issues/100218): When [`socket.if_nametoindex()`](https://docs.python.org/3.14/library/socket.html#socket.if_nametoindex) or [`socket.if_indextoname()`](https://docs.python.org/3.14/library/socket.html#socket.if_indextoname) throws an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), the [`errno`](https://docs.python.org/3.14/library/exceptions.html#OSError.errno) value is now set properly. Bénédikt Tran contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
