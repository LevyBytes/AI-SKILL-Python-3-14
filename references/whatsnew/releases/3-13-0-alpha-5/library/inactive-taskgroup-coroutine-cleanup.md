# Python 3.13.0 alpha 5 / library / inactive taskgroup coroutine cleanup

[gh-115957](https://github.com/python/cpython/issues/115957): Whenever `asyncio.TaskGroup.create_task` is invoked on an inactive `asyncio.TaskGroup`, the coroutine handed in gets closed (heading off a `RuntimeWarning`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
