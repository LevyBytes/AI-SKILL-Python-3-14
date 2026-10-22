# Error handling API

### Error handling API

Lets you tailor the way exceptions get processed within the event loop.

 loop.set_exception_handler(*handler*)

Install *handler* to serve as the event loop's exception handler going forward.

Passing `None` for *handler* restores the default exception handler. Otherwise *handler* has to be a callable whose signature matches `(loop, context)`, in which `loop` points at the running event loop and `context` is a `dict` object holding the exception's details (the `call_exception_handler()` documentation explains what context carries).

When the handler runs in response to a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) or `Handle`, it executes within the [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) belonging to that task or callback handle.

Changed in version 3.12: The handler can now run inside the [`Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) belonging to whichever task or handle gave rise to the exception.

 loop.get_exception_handler()

Hand back whatever exception handler is in effect, or `None` when no custom one has been installed.

Added in version 3.5.2.

 loop.default_exception_handler(*context*)

Default exception handler.

Triggered whenever an exception arises while no exception handler is configured. A custom exception handler may also invoke it directly when it wishes to fall back on the default behavior.

The *context* argument carries the same meaning it has in `call_exception_handler()`.

 loop.call_exception_handler(*context*)

Invoke the event loop's exception handler that is currently active.

The *context* is a `dict` object holding the keys listed below (later Python releases may add further keys):

- ‘message’: Error message;

- ‘exception’ (optional): Exception object;

- ‘future’ (optional): [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) instance;

- ‘task’ (optional): [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) instance;

- ‘handle’ (optional): `asyncio.Handle` instance;

- ‘protocol’ (optional): [Protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) instance;

- ‘transport’ (optional): [Transport](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-transport) instance;

- ‘socket’ (optional): [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) instance;

- ‘source_traceback’ (optional): Traceback of the source;

- ‘handle_traceback’ (optional): Traceback of the handle;

- ‘asyncgen’ (optional): Asynchronous generator that caused

the exception.

Note

Do not override this method when subclassing an event loop. To handle exceptions yourself, rely on the `set_exception_handler()` method.

[Subject index](INDEX.md) · [Previous](loop-set-default-executor.md) · [Continue](loop-get-debug-to-loop-slow-callback-duration.md)
