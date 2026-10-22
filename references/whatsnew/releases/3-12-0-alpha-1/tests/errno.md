# Python 3.12.0 alpha 1 / tests / errno

[gh-95573](https://github.com/python/cpython/issues/95573): [Lib/test/test_asyncio/test_ssl.py](https://github.com/python/cpython/tree/3.14/Lib/test/test_asyncio/test_ssl.py) revealed a macOS kernel bug where heavy concurrent load over non-blocking sockets sometimes triggers [`errno.ENOBUFS`](https://docs.python.org/3.14/library/errno.html#errno.ENOBUFS) ("No buffer space available"). FB11063974 was filed with Apple; meanwhile, as a stopgap, the buffer size used by macOS tests is lowered to dodge sporadic failures. Fantix King contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
