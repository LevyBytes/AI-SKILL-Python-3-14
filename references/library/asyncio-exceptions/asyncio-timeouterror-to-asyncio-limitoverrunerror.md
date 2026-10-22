# Exceptions

# Asyncio Exceptions, Asyncio Extending, Asyncio Future, Asyncio Graph

## Overview

Covers: Exceptions; Extending; Futures; Call Graph Introspection.

## Exceptions

### Exceptions

**Source code:** [Lib/asyncio/exceptions.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/exceptions.py)

---

 *exception *asyncio.TimeoutError

A now-deprecated alias for `TimeoutError`; it surfaces once an operation overruns the deadline it was given.

Changed in version 3.11: This class became an alias for `TimeoutError`.

 *exception *asyncio.CancelledError

Signals that the operation was cancelled.

You may intercept this exception to run cleanup logic whenever asyncio Tasks get cancelled, though in nearly every case you are expected to re-raise it afterward.

Changed in version 3.8: `CancelledError` now derives from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) instead of [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception).

 *exception *asyncio.InvalidStateError

Indicates a corrupt internal state inside a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) or [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future).

One way this surfaces is trying to assign a result to a *Future* object whose result has already been populated.

 *exception *asyncio.SendfileNotAvailableError

The “sendfile” syscall cannot be applied to this particular socket or file kind.

This is a subclass of [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 *exception *asyncio.IncompleteReadError

The read that was asked for finished only partway.

Raised by the [asyncio stream APIs](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-streams).

It derives from [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError).

 expected

How many bytes were anticipated in total, as an [`int`](https://docs.python.org/3.14/library/functions.html#int).

 partial

Those [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) that had already been read by the time the stream ended.

 *exception *asyncio.LimitOverrunError

Hit the configured buffer-size ceiling before a separator could be found.

Raised by the [asyncio stream APIs](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-streams).

 consumed

The count of bytes slated to be consumed.

[Subject index](INDEX.md) · [Continue](../asyncio-extending/extending.md)
