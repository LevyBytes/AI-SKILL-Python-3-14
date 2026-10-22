# Eager task factory

### Eager task factory

 asyncio.eager_task_factory(*loop*, *coro*, ***, *name=None*, *context=None*)

A task factory for eager task execution.

With this factory in use (through [`loop.set_task_factory(asyncio.eager_task_factory)`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory)), coroutines start running synchronously as the `Task` is being constructed. A task only lands on the event loop's schedule if it ends up blocking. This may yield a performance gain, since the cost of loop scheduling is sidestepped for coroutines that finish synchronously.

One frequent scenario where this pays off is coroutines that rely on caching or memoization to skip real I/O whenever they can.

Note

Running the coroutine right away amounts to a semantic shift. Where the coroutine returns or raises, the task never gets scheduled onto the event loop. Where the coroutine's execution blocks, the task is scheduled onto the event loop. Such a shift could bring about behavior changes in existing applications. For one, the order in which an application's tasks execute will probably change.

Added in version 3.12.

 asyncio.create_eager_task_factory(*custom_task_constructor*)

Build an eager task factory, much like `eager_task_factory()`, that draws on the given *custom_task_constructor* to make a new task in place of the default `Task`.

The *custom_task_constructor* has to be a *callable* whose signature lines up with the signature of `Task.__init__`. That callable is required to return an object compatible with `asyncio.Task`.

What this function returns is a *callable* meant for use as an event loop's task factory by way of [`loop.set_task_factory(factory)`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory)).

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](running-tasks-concurrently.md) · [Continue](shielding-from-cancellation.md)
