# Task cancellation

### Task cancellation

Cancelling tasks can be done readily and safely. Once a task gets cancelled, [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) is raised inside that task at the earliest chance.

The advice is for coroutines to wrap clean-up logic in `try/finally` blocks so it runs reliably. Whenever [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) gets caught on purpose, the usual practice is to re-raise it after the clean-up finishes. Because `asyncio.CancelledError` is a direct subclass of [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException), the majority of code needn't concern itself with it.

Those asyncio pieces that provide structured concurrency, such as `asyncio.TaskGroup` and `asyncio.timeout()`, rely on cancellation under the hood and may behave incorrectly should a coroutine swallow [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError). By the same token, calling `uncancel` from user code is generally inadvisable. That said, where genuinely suppressing `asyncio.CancelledError` is what you want, you must additionally invoke `uncancel()` so the cancellation state is fully cleared.

[Subject index](INDEX.md) · [Previous](asyncio-create-task.md) · [Continue](asyncio-taskgroup-class.md)
