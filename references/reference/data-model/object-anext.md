# object.__anext__(*self*)

object.__anext__(*self*)

Has to give back an *awaitable* that resolves to the iterator's following value. Once iteration runs out, it ought to raise a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) error.

Here is a sample asynchronous iterable object:

```python
class Reader:
    async def readline(self):
        ...

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

```

Added in version 3.5.

Changed in version 3.7: In Python releases before 3.7, it was permitted for `__aiter__()` to hand back an *awaitable* resolving into an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator).

From Python 3.7 onward, an asynchronous iterator object is what `__aiter__()` is required to produce. Hand back anything different and a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) error follows.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Owning language section](asynchronous-iterators.md) · [Previous source section](object-aiter.md) · [Following source section](asynchronous-context-managers.md)
