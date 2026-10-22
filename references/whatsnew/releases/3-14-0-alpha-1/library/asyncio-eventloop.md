# Python 3.14.0 alpha 1 / library / asyncio eventloop

[gh-113892](https://github.com/python/cpython/issues/113892): The `sock_connect` method of [`asyncio.ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the given socket is not in non-blocking mode, matching what the other loop implementations already do.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
