# Introspection

### Introspection

 asyncio.current_task(*loop=None*)

Return the currently running `Task` instance, or `None` if no task is running.

When *loop* is `None`, [`get_running_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_running_loop) supplies the current loop.

Added in version 3.7.

 asyncio.all_tasks(*loop=None*)

Return a set of not yet finished `Task` objects run by the loop.

When *loop* is `None`, the current loop comes from [`get_running_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_running_loop).

Added in version 3.7.

 asyncio.iscoroutine(*obj*)

Return `True` if *obj* is a coroutine object.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](asyncio-run-coroutine-threadsafe.md) · [Continue](asyncio-task-class.md)
