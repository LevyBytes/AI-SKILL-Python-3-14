# Python 3.14.5 release candidate 1 / security / asyncio eventloop

[gh-148808](https://github.com/python/cpython/issues/148808): Introduced a buffer-boundary check for the `nbytes` argument passed to `asyncio.AbstractEventLoop.sock_recvfrom_into()`. This matters only on Windows together with the [`asyncio.ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
