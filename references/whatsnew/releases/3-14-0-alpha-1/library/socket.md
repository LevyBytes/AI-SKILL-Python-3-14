# Python 3.14.0 alpha 1 / library / socket

[gh-124944](https://github.com/python/cpython/issues/124944): Introduces `SO_ORIGINAL_DST` into the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module.

[gh-84808](https://github.com/python/cpython/issues/84808): Repairs error handling in the [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) method [`connect_ex()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect_ex) on platforms where `errno` is allowed to go negative.

[gh-121423](https://github.com/python/cpython/issues/121423): Shorten the import time of [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) by deferring module imports and turning `socket.errorTab` into a constant.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
