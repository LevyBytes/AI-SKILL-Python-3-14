# Creating tasks

### Creating tasks

**Source code:** [Lib/asyncio/tasks.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/tasks.py)

---

 asyncio.create_task(*coro*, ***, *name=None*, *context=None*, *eager_start=None*, ***kwargs*)

Enclose the *coro* coroutine inside a `Task` and queue it to execute. The Task object is returned.

For the most part, this function's complete signature mirrors the one for the `Task` constructor (or factory) - every keyword argument given here is forwarded straight to that interface.

A keyword-only *context* argument is optional and lets you designate a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) within which the *coro* will run. Whenever no *context* gets supplied, a copy of the present context is generated.

There is also an optional keyword-only *eager_start* argument that lets you state whether the task ought to run eagerly while create_task is being called, or instead be queued for later. Should *eager_start* go unsupplied, whatever mode was established by [`loop.set_task_factory()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory) takes effect.

Execution of the task happens within the loop given back by [`get_running_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_running_loop); a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) gets raised whenever the current thread has no running loop.

Note

Built on structured concurrency, `asyncio.TaskGroup.create_task()` is a newer option; it lets you await a set of related tasks while giving strong safety guarantees.

Important

Hold onto a reference to whatever this function returns, so that a task doesn't vanish partway through running. Tasks are tracked by the event loop with weak references only. Any task not referenced from somewhere else is liable to be garbage collected at any moment, possibly before finishing. To make “fire-and-forget” background tasks dependable, collect them into a container:

```python
background_tasks = set()

for i in range(10):
    task = asyncio.create_task(some_coro(param=i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)

```

Added in version 3.7.

Changed in version 3.8: Added the *name* parameter.

Changed in version 3.11: Added the *context* parameter.

Changed in version 3.14: Added the *eager_start* parameter by passing on all *kwargs*.

[Subject index](INDEX.md) · [Previous](awaitables.md) · [Continue](task-cancellation.md)
