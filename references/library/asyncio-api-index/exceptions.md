# asyncio — Exceptions

### Exceptions

| `asyncio.CancelledError` | Thrown once a Task gets cancelled. Refer as well to `Task.cancel()`. |
| --- | --- |
| `asyncio.BrokenBarrierError` | Thrown once a Barrier gets broken. Refer as well to `Barrier.wait()`. |

Examples

- [Handling CancelledError to run code on cancellation request](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-task-cancel).

- See also the full list of [asyncio-specific exceptions](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio-exceptions).

[Subject index](INDEX.md) · [Previous](synchronization.md) · [Continue](../asyncio-dev/developing-with-asyncio.md)
