# asyncio.policy: `get_event_loop()`, `set_event_loop()`, `new_event_loop()`

get_event_loop()

Get the event loop for the current context.

Return an event loop object implementing the [`AbstractEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.AbstractEventLoop) interface.

This method should never return `None`.

Changed in version 3.6.

 set_event_loop(*loop*)

Set the event loop for the current context to *loop*.

 new_event_loop()

Create and return a new event loop object.

This method should never return `None`.

Deprecated since version 3.14: Now deprecated, the `AbstractEventLoopPolicy` class is set for removal in Python 3.16.

The built-in policies that ship with asyncio are:

[Subject index](INDEX.md) · [Previous](asyncio-abstracteventlooppolicy-class.md) · [Continue](asyncio-defaulteventlooppolicy-class.md) · [Owning module, declaration or section: asyncio.AbstractEventLoopPolicy](asyncio-abstracteventlooppolicy-class.md) · [Owning module, declaration or section: Policy Objects](asyncio-abstracteventlooppolicy-class.md)
