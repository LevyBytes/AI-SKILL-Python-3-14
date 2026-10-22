# Exceptions

### Exceptions

 *exception *asyncio.QueueEmpty

Calling the `get_nowait()` method on a queue that holds nothing is what triggers this exception.

 *exception *asyncio.QueueFull

The exception thrown when `put_nowait()` is invoked against a queue that has already hit its *maxsize*.

 *exception *asyncio.QueueShutDown

The exception thrown when either `put()` or `get()` runs against a queue that is already shut down.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](asyncio-lifoqueue-class.md) · [Continue](examples.md)
