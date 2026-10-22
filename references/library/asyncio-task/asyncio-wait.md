# asyncio.task: `asyncio.wait()`

### Waiting primitives

 *async *asyncio.wait(*aws*, ***, *timeout=None*, *return_when=ALL_COMPLETED*)

Run the [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) and `Task` objects from the *aws* iterable side by side, blocking until the *return_when* condition holds.

There must be at least one item in the *aws* iterable.

Hands back a pair of Task/Future sets: `(done, pending)`.

Usage:

```python
done, pending = await asyncio.wait(aws)

```

When given, *timeout* (a float or int) caps how many seconds elapse before the call comes back.

Be aware that this function will not raise [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError). Any Futures or Tasks still unfinished at the timeout simply land in the second set.

*return_when* states the point at which the call returns. Its value has to be one of these constants:

| Constant | Description |
| --- | --- |
| asyncio.FIRST_COMPLETED | The call comes back the moment any future completes or gets cancelled. |
| asyncio.FIRST_EXCEPTION | The call comes back as soon as some future ends by raising an exception. Where not a single future raises one, the behavior matches `ALL_COMPLETED`. |
| asyncio.ALL_COMPLETED | The call comes back once every future has finished or been cancelled. |

In contrast to `wait_for()`, a timeout in `wait()` leaves the futures uncancelled.

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Passing coroutine objects to `wait()` directly is forbidden.

Changed in version 3.12: Added support for generators yielding tasks.

[Subject index](INDEX.md) · [Previous](asyncio-wait-for.md) · [Continue](asyncio-as-completed.md)
