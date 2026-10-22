# Python 3.13.0 alpha 3 / library / asyncio task

[gh-113848](https://github.com/python/cpython/issues/113848): The [`asyncio.TaskGroup()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) and [`asyncio.timeout()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.timeout) context managers will now cope with [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) subclasses on top of the exact `CancelledError`.

[gh-112622](https://github.com/python/cpython/issues/112622): Guarantee that the `name` parameter reaches the event loop in [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
