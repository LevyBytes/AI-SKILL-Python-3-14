# Python 3.14.0 alpha 1 / library / asyncio task

[gh-124958](https://github.com/python/cpython/issues/124958): Resolves reference cycles among exceptions thrown by [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) plus the python rendition of [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future)

[gh-122332](https://github.com/python/cpython/issues/122332): Cleared up a segfault tied to [`asyncio.Task.get_coro()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.get_coro) under an eager task factory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
