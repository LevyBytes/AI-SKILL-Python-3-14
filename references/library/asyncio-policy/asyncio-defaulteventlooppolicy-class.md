# asyncio.policy: `asyncio.DefaultEventLoopPolicy`

*class *asyncio.DefaultEventLoopPolicy

The default asyncio policy. Uses [`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) on Unix and [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) on Windows.

You do not have to install the default policy yourself. asyncio sets itself up to apply the default policy automatically.

Changed in version 3.8: Under Windows, [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) now serves as the default.

Changed in version 3.14: When no event loop has been set, the default asyncio policy's [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) method now raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Deprecated since version 3.14: Now deprecated, the `DefaultEventLoopPolicy` class is bound for removal in Python 3.16.

[Subject index](INDEX.md) · [Previous](policy-event-loop-access-and-creation.md) · [Continue](asyncio-windowsselectoreventlooppolicy-class.md) · [Owning module, declaration or section: Policy Objects](asyncio-abstracteventlooppolicy-class.md)
