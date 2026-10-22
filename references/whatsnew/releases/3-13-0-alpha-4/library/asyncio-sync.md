# Python 3.13.0 alpha 4 / library / asyncio sync

[gh-112202](https://github.com/python/cpython/issues/112202): Make certain an [`asyncio.Condition.notify()`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Condition.notify) invocation is not dropped should the woken `Task` be cancelled at the same moment or hit some other error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
