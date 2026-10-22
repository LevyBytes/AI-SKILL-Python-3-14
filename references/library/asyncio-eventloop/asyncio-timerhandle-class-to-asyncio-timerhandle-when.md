# asyncio.eventloop: `asyncio.TimerHandle`, `when()`

*class *asyncio.TimerHandle

A callback wrapper object returned by `loop.call_later()`, and `loop.call_at()`.

This class is a subclass of `Handle`.

 when()

Return a scheduled callback time as [`float`](https://docs.python.org/3.14/library/functions.html#float) seconds.

That time is an absolute timestamp expressed against the same time reference that `loop.time()` uses.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](asyncio-handle-get-context-to-asyncio-handle-cancelled.md) · [Continue](asyncio-server-class.md) · [Owning module, declaration or section: Callback handles](asyncio-handle-class.md)
