# Python 3.12.0 alpha 4 / library / asyncio

[gh-100133](https://github.com/python/cpython/issues/100133): Repair an [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) regression in which a subprocess would occasionally drop data it had read from a pipe.

[gh-91166](https://github.com/python/cpython/issues/91166): [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) was tuned to cut needless copying on socket writes and to call [`sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg) where the platform offers it. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
