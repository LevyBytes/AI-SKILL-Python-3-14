# Python 3.13.0 alpha 3 / library / asyncio sync

[gh-111693](https://github.com/python/cpython/issues/111693): [`asyncio.Condition.wait()`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Condition.wait) will now re-raise the very same `CancelledError` instance that may have interrupted it. A race condition within [`asyncio.Semaphore.acquire()`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Semaphore.acquire) when interrupted by a `CancelledError` was fixed too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
