# Python 3.13.0 alpha 1 / library / asyncio task

[gh-105684](https://github.com/python/cpython/issues/105684): Third-party task implementations are now required to back [`asyncio.Task.set_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.set_name). The undocumented `_set_task_name()` function, deprecated as far back as 3.8, is gone. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
