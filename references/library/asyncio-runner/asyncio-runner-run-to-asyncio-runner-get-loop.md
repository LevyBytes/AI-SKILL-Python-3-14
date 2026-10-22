# asyncio.runner: `run()`, `close()`, `get_loop()`

run(*coro*, ***, *context=None*)

Execute *coro* in the embedded event loop.

The argument can be any awaitable object.

Should that argument be a coroutine, it gets wrapped inside a Task.

There is an optional keyword-only *context* argument that lets you name a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) for the code to execute within. Leave context at `None` and the runner's own default context applies.

Hands back the awaitable's result, or else raises an exception.

Invoking this function is not allowed while a separate asyncio event loop is already active on the same thread.

Changed in version 3.14: *coro* can be any awaitable object.

 close()

Close the runner.

Finalizes the asynchronous generators, shuts down the default executor, closes the event loop, and lets go of the embedded [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context).

 get_loop()

Return the event loop associated with the runner instance.

Note

`Runner` follows a lazy-initialization approach, so its constructor leaves the underlying low-level structures uninitialized.

The embedded *loop* and *context* come into being either as the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) body is entered or upon the first `run()` or `get_loop()` call, whichever happens first.

[Subject index](INDEX.md) · [Previous](asyncio-runner-class.md) · [Continue](handling-keyboard-interruption.md) · [Owning module, declaration or section: asyncio.Runner](asyncio-runner-class.md) · [Owning module, declaration or section: Runner context manager](asyncio-runner-class.md)
