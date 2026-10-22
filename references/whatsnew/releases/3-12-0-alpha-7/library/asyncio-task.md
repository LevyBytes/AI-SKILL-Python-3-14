# Python 3.12.0 alpha 7 / library / asyncio task

[gh-102780](https://github.com/python/cpython/issues/102780): The [`asyncio.Timeout`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Timeout) context manager now behaves dependably even while cleaning up after a task cancellation. Formerly it might surface a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) where a [`TimeoutError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.TimeoutError) was expected.

[gh-78530](https://github.com/python/cpython/issues/78530): [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait) will now take generators that yield tasks. Kumar Aditya wrote the patch.

[gh-102748](https://github.com/python/cpython/issues/102748): [`asyncio.iscoroutine()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.iscoroutine) now answers `False` for generators, since [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) has no support for legacy generator-based coroutines. Kumar Aditya wrote the patch.

[gh-100112](https://github.com/python/cpython/issues/100112): When wrapping an awaitable object, [`asyncio.Task.get_coro()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.get_coro) is now guaranteed to hand back a coroutine. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
