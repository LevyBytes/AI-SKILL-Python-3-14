# Python 3.13.0 alpha 3 / library / socket

[gh-81194](https://github.com/python/cpython/issues/81194): Stop a crash in [`socket.if_indextoname()`](https://docs.python.org/3.14/library/socket.html#socket.if_indextoname) when handed a particular value (UINT_MAX). Also fix an integer overflow inside `socket.if_indextoname()` on 64-bit non-Windows platforms.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
