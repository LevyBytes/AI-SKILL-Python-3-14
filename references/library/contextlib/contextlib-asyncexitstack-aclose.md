# contextlib.AsyncExitStack: `aclose()`

Acts like `ExitStack.callback()`, except that it wants a coroutine function instead.

 *async *aclose()

Acts like `ExitStack.close()`, but deals with awaitables the right way.

Continuing the example for `asynccontextmanager()`:

```python
async with AsyncExitStack() as stack:
    connections = [await stack.enter_async_context(get_connection())
        for i in range(5)]
    # All opened connections will automatically be released at the end of
    # the async with statement, even if attempts to open a connection
    # later in the list raise an exception.

```

Added in version 3.7.

[Subject index](INDEX.md) · [Continue](examples-and-recipes.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: contextlib.AsyncExitStack](async-exit-stack-contexts-and-callbacks.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md) · [Owning module, declaration or section: push_async_callback](async-exit-stack-contexts-and-callbacks.md) · [Preceding source contract and version conditions](async-exit-stack-contexts-and-callbacks.md)
