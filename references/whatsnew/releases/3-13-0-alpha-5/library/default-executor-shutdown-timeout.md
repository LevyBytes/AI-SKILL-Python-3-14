# Python 3.13.0 alpha 5 / library / default executor shutdown timeout

[gh-111358](https://github.com/python/cpython/issues/111358): Repair a bug inside `asyncio.BaseEventLoop.shutdown_default_executor()` so the timeout fed to the coroutine acts as intended.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
