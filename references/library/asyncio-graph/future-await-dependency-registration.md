# Low level utility functions

### Low level utility functions

For asyncio to introspect an async call graph, it needs help from the control-flow constructs, things like [`shield()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.shield) or [`TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup). Whenever an in-between [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) object that relies on low-level APIs such as [`Future.add_done_callback()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.add_done_callback) comes into play, the pair of functions below should tell asyncio precisely how those intermediate future objects relate to the tasks they enclose or steer.

 `asyncio.future_add_to_awaited_by(*future*, *waiter*, */*)`

Note down that *future* is being awaited by *waiter*.

Each of *future* and *waiter* has to be an instance of [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) or [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task), or of a subclass of either; if not, the call simply does nothing.

Every `future_add_to_awaited_by()` call has to be paired, eventually, with a matching `future_discard_from_awaited_by()` call carrying the same arguments.

 `asyncio.future_discard_from_awaited_by(*future*, *waiter*, */*)`

Note down that *future* is no longer being awaited by *waiter*.

Each of *future* and *waiter* has to be an instance of [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) or [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task), or of a subclass of either; if not, the call simply does nothing.

[Subject index](INDEX.md) · [Previous](framecallgraphentry.md)
