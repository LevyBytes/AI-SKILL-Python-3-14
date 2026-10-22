# asyncio.future: `asyncio.Future`

### Future Object

 *class *asyncio.Future(***, *loop=None*)

A Future stands in for the result an asynchronous operation will eventually yield. It is not thread-safe.

A Future is an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object: coroutines can keep awaiting a Future until it carries a result, carries an exception, or gets cancelled. The same Future may be awaited more than once, and each time the result it returns is identical.

Most often Futures let low-level callback-based code (for instance, protocols built on asyncio [transports](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-transports-protocols)) cooperate with high-level async/await code.

As a guideline, keep Future objects out of any user-facing API, and build one by calling [`loop.create_future()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_future). Doing so lets alternative event loop implementations supply their own tuned versions of a Future object.

Futures are [generic](https://docs.python.org/3.14/library/typing.html#generics) with respect to the type their results take.

Changed in version 3.7: Gained support for the [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars) module.

Deprecated since version 3.10: A deprecation warning fires when *loop* goes unspecified and no event loop is running.

[Subject index](INDEX.md) · [Previous](asyncio-isfuture-to-asyncio-wrap-future.md) · [Continue](asyncio-future-result-to-asyncio-future-cancel.md)
