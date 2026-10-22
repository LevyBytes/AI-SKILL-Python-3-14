# Python 3.13.0 beta 1 / library / overview

Where a task group gets cancelled from outside and additionally has to raise an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup), it now invokes the parent task's [`cancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel) method. Doing so guarantees that an [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) will surface at the following [`await`](https://docs.python.org/3.14/reference/expressions.html#await), keeping the cancellation from being lost.

A further upside of these adjustments is that task groups now keep the cancellation count intact ([`asyncio.Task.cancelling()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancelling)).

So that some edge cases are covered, [`asyncio.Task.uncancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.uncancel) may now clear the undocumented `_must_cancel` flag once the cancellation count returns to zero.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
