# Subprocess and Threads

### Subprocess and Threads

By default, the standard asyncio event loop supports running subprocesses from different threads.

On Windows subprocesses come from [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) alone (the default); [`SelectorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.SelectorEventLoop) carries no subprocess support.

Keep in mind that other event loop implementations may impose their own constraints; check their documentation for the details.

See also

The [Concurrency and multithreading in asyncio](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading) section.

[Subject index](INDEX.md) · [Previous](interacting-with-subprocesses.md) · [Continue](examples.md)
