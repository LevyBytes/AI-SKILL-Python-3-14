# contextlib: `contextlib.AsyncContextDecorator`

*class *contextlib.AsyncContextDecorator

Comparable to `ContextDecorator`, though confined to asynchronous functions.

An example of `AsyncContextDecorator`:

```python
from asyncio import run
from contextlib import AsyncContextDecorator

class mycontext(AsyncContextDecorator):
    async def __aenter__(self):
        print('Starting')
        return self

    async def __aexit__(self, *exc):
        print('Finishing')
        return False

```

Afterward, the class can be applied like so:

```python
>>> @mycontext()
... async def function():
...     print('The bit in the middle')
...
>>> run(function())
Starting
The bit in the middle
Finishing

>>> async def function():
...    async with mycontext():
...         print('The bit in the middle')
...
>>> run(function())
Starting
The bit in the middle
Finishing

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](contextlib-contextdecorator-class.md) · [Continue](contextlib-exitstack-class-to-contextlib-exitstack-close.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)
