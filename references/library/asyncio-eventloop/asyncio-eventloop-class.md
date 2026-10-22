# asyncio.eventloop: `asyncio.EventLoop`

*class *asyncio.EventLoop

>

An alias pointing to whichever `AbstractEventLoop` subclass performs best on the current platform.

It maps to `SelectorEventLoop` under Unix and to `ProactorEventLoop` under Windows.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](asyncio-proactoreventloop-class.md) · [Continue](asyncio-abstracteventloop-class.md) · [Owning module, declaration or section: Event loop implementations](asyncio-selectoreventloop-class.md)
