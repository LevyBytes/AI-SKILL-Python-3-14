# Python 3.13.0 alpha 2 / library / asyncio task

[gh-110910](https://github.com/python/cpython/issues/110910): Repair broken state handling within [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) and [`asyncio.Timeout`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Timeout). When misused they now raise a proper RuntimeError and remain in a consistent state afterward.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
