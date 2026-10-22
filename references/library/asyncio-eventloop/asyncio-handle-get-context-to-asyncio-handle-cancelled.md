# asyncio.eventloop: `get_context()`, `cancel()`, `cancelled()`

get_context()

Return the [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object associated with the handle.

Added in version 3.12.

 cancel()

Cancel the scheduled callback. The method does nothing if that callback was already canceled or has already run.

 cancelled()

Return `True` if the callback was cancelled.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](asyncio-handle-class.md) · [Continue](asyncio-timerhandle-class-to-asyncio-timerhandle-when.md) · [Owning module, declaration or section: asyncio.Handle](asyncio-handle-class.md) · [Owning module, declaration or section: Callback handles](asyncio-handle-class.md)
