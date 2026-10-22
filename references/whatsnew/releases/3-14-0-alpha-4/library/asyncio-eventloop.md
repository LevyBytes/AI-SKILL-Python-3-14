# Python 3.14.0 alpha 4 / library / asyncio eventloop

[gh-128552](https://github.com/python/cpython/issues/128552): Eliminated the cyclic garbage that [`asyncio.loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task) and [`asyncio.TaskGroup.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup.create_task) produced by keeping a reference to a created task whenever it was eager.

[gh-128340](https://github.com/python/cpython/issues/128340): Added an internal thread-safe handle for use by [`asyncio.loop.call_soon_threadsafe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe) so cancellation can happen safely across threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
