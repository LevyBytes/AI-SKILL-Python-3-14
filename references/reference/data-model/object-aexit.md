# object.__aexit__(*self*, *exc_type*, *exc_value*, *traceback*)

object.__aexit__(*self*, *exc_type*, *exc_value*, *traceback*)

Mirrors `__exit__()` in meaning, the sole distinction being that an *awaitable* must come back from it.

Below is a sample asynchronous context manager class:

```python
class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')

```

Added in version 3.5.

Footnotes

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Owning language section](asynchronous-context-managers.md) · [Previous source section](object-aenter.md)
