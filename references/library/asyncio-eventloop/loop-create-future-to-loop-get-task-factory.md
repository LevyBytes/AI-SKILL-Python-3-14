# Creating futures and tasks

### Creating futures and tasks

 loop.create_future()

Create an [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) object attached to the event loop.

In asyncio, this is the recommended route for creating Futures. It allows third-party event loops to supply their own Future object implementations (offering better performance or instrumentation).

Added in version 3.5.2.

 loop.create_task(*coro*, ***, *name=None*, *context=None*, *eager_start=None*, ***kwargs*)

Schedule the execution of [coroutine](https://docs.python.org/3.14/library/asyncio-task.html#coroutine) *coro*. Return a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) object.

For interoperability, third-party event loops may supply their own [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) subclass. When that happens, the returned type is a subclass of `Task`.

By and large the complete function signature mirrors that of the [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) constructor (or factory) - every keyword argument given to this function is forwarded to that interface.

Whenever the *name* argument is supplied and is not `None`, it becomes the task’s name through [`Task.set_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.set_name).

Through an optional keyword-only *context* argument you can designate a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) in which the *coro* runs. When no *context* is supplied, a copy of the current context is made.

Through an optional keyword-only *eager_start* argument you can state whether the task runs eagerly during the create_task call or gets scheduled for later. Omitting *eager_start* falls back to whatever mode `loop.set_task_factory()` established.

Changed in version 3.8: Added the *name* parameter.

Changed in version 3.11: Added the *context* parameter.

Changed in version 3.13.3: Introduced `kwargs`, forwarding arbitrary additional parameters such as `name` and `context`.

Changed in version 3.13.4: Reverted forwarding of *name* and *context* (when None), yet kept forwarding the rest of the arbitrary keyword arguments, so as not to break backwards compatibility with 3.13.3.

Changed in version 3.14: Every *kwargs* entry is forwarded now. The *eager_start* parameter operates together with eager task factories.

 loop.set_task_factory(*factory*)

Set a task factory that will be used by `loop.create_task()`.

When *factory* is `None`, the default task factory takes effect. Otherwise *factory* has to be a *callable* whose signature matches `(loop, coro, **kwargs)`, in which *loop* points to the active event loop and *coro* is a coroutine object. That callable has to forward all *kwargs* and yield an [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task)-compatible object.

Changed in version 3.13.3: Made it mandatory that every *kwargs* entry be forwarded to [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).

Changed in version 3.13.4: Task factories stop receiving *name*. They also stop receiving *context* whenever its value is `None`.

Changed in version 3.14: Both *name* and *context* are once more forwarded to task factories without any condition.

 loop.get_task_factory()

Return a task factory or `None` if the default one is in use.

[Subject index](INDEX.md) · [Previous](loop-call-later-to-loop-time.md) · [Continue](network-connection-overview.md)
