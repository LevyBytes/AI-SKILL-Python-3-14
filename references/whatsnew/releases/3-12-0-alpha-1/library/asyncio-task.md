# Python 3.12.0 alpha 1 / library / asyncio task

[gh-95289](https://github.com/python/cpython/issues/95289): [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) is corrected so it forwards an exception whenever a context manager swaps [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) for some other exception. Kumar Aditya and Guido van Rossum wrote the patch.

[gh-95109](https://github.com/python/cpython/issues/95109): Timeouts arranged via [`asyncio.Timeout`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Timeout) that already lapsed are now delivered without delay.

[gh-94398](https://github.com/python/cpython/issues/94398): Once an [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) begins its shutdown (that is, at least one task failed and the task group started cancelling whatever tasks remain), adding new tasks to that task group should no longer be allowed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
