# asyncio.task: `asyncio.Task`

### Task object

 *class *asyncio.Task(*coro*, ***, *loop=None*, *name=None*, *context=None*, *eager_start=False*)

A [`Future-like`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) object that runs a Python coroutine. Not thread-safe.

A Task exists to drive a coroutine inside an event loop. Whenever a coroutine awaits a Future, the Task pauses the coroutine and holds until that Future finishes. After the Future reaches the *done* state, the wrapped coroutine picks back up.

Cooperative scheduling drives event loops: a single Task runs at any given moment in an event loop. As one Task waits on a Future to finish, the event loop turns to other Tasks, callbacks, or IO work.

Create Tasks with the high-level `asyncio.create_task()` function, or with the low-level [`loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task) or [`ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) functions. Building Tasks by hand is not recommended.

Cancel a Task that is running by calling its `cancel()` method. Doing so throws a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception into the wrapped coroutine. Where a coroutine is awaiting a Future object as cancellation arrives, that Future object is cancelled as well.

To find out whether a Task was cancelled, use `cancelled()`. It yields `True` whenever the wrapped coroutine let the [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception through and the cancellation actually took effect.

`asyncio.Task` inherits from [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) all of its APIs except [`Future.set_result()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.set_result) and [`Future.set_exception()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.set_exception).

A keyword-only *context* argument is optional and lets you name a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) in which the *coro* should run. Absent a *context*, the Task duplicates the current context and afterward runs its coroutine within that copy.

A keyword-only *eager_start* argument is also optional and lets the `asyncio.Task` begin running the moment the task is created. With `True` set and the event loop already running, the task starts the coroutine at once and keeps going until the coroutine first blocks. When the coroutine returns or raises before ever blocking, the task completes eagerly and never gets scheduled onto the event loop.

Tasks are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the return type of their wrapped coroutines.

Changed in version 3.7: Added support for the [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) module.

Changed in version 3.8: Added the *name* parameter.

Deprecated since version 3.10: A deprecation warning fires whenever *loop* goes unspecified while no event loop is running.

Changed in version 3.11: Added the *context* parameter.

Changed in version 3.12: Added the *eager_start* parameter.

[Subject index](INDEX.md) · [Previous](asyncio-current-task-to-asyncio-iscoroutine.md) · [Continue](asyncio-task-done-to-asyncio-task-get-context.md)
