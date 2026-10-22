# Python 3.14.0 alpha 2 / library / asyncio eventloop

[gh-125969](https://github.com/python/cpython/issues/125969): Fix an out-of-bounds crash triggered when a malicious [`asyncio.loop.call_soon()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon) alters the length belonging to the internal callbacks list. Bénédikt Tran wrote the patch.

[gh-126353](https://github.com/python/cpython/issues/126353): Calling [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) will no longer build an event loop behind the scenes. A [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised whenever no event loop has been set. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
