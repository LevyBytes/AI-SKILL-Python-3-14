# asyncio.eventloop: `asyncio.SelectorEventLoop`

### Event loop implementations

Two distinct event loop implementations come with asyncio: `SelectorEventLoop` and `ProactorEventLoop`.

asyncio's out-of-the-box configuration selects `EventLoop`.

 *class *asyncio.SelectorEventLoop

A subclass of `AbstractEventLoop` based on the [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) module.

It draws on the best-performing *selector* the platform offers. You can also pin down exactly which selector implementation gets used:

```python
import asyncio
import selectors

async def main():
   ...

loop_factory = lambda: asyncio.SelectorEventLoop(selectors.SelectSelector())
asyncio.run(main(), loop_factory=loop_factory)

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

[Subject index](INDEX.md) · [Previous](server-objects.md) · [Continue](asyncio-proactoreventloop-class.md)
