# asyncio.future: `result()`, `set_result()`, `set_exception()`, `done()`, `cancelled()`, `add_done_callback()`, `remove_done_callback()`, `cancel()`

result()

Hand back the Future's result.

When the Future is *done* and a result was placed on it via the `set_result()` method, that stored value comes back.

When the Future is *done* but `set_exception()` recorded an exception on it, this method re-raises that exception.

When the Future sits in the *cancelled* state, this method throws a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception.

When the Future’s result has not arrived yet, this method throws an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) exception.

 set_result(*result*)

Flag the Future as *done* and store its result.

Throws an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) error should the Future already be *done*.

 set_exception(*exception*)

Flag the Future as *done* and attach an exception to it.

Throws an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) error should the Future already be *done*.

 done()

Yield `True` when the Future is *done*.

A Future counts as *done* once it has been *cancelled*, or once a `set_result()` or `set_exception()` call has given it a result or an exception.

 cancelled()

Yield `True` when the Future has been *cancelled*.

You typically reach for this method to confirm a Future is not *cancelled* before you assign it a result or an exception:

```python
if not fut.cancelled():
    fut.set_result(42)

```

 add_done_callback(*callback*, ***, *context=None*)

Register a callback that fires once the Future reaches *done*.

When invoked, the *callback* receives the Future object as its sole argument.

Should the Future already be *done* at the moment this method runs, the callback gets queued through [`loop.call_soon()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon).

There is an optional keyword-only *context* argument that lets you hand the *callback* a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) to execute within. Omit *context* and the present context is used instead.

To feed arguments to the callback, [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) comes in handy, for example:

```python
# Call 'print("Future:", fut)' when "fut" is done.
fut.add_done_callback(
    functools.partial(print, "Future:"))

```

Changed in version 3.7: Introduced the *context* keyword-only parameter. Refer to [**PEP 567**](https://peps.python.org/pep-0567/) for the full details.

 remove_done_callback(*callback*)

Drop *callback* from the list of callbacks.

Gives back how many callbacks were dropped — ordinarily 1, except where the same callback had been registered repeatedly.

 cancel(*msg=None*)

Cancel the Future and queue its callbacks.

Where the Future is already *done* or *cancelled*, the call returns `False`. Otherwise it flips the Future’s state to *cancelled*, queues the callbacks, and returns `True`.

That optional string *msg* argument becomes the argument handed to the [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception thrown when a cancelled Future is later awaited.

Changed in version 3.9: Introduced the *msg* parameter.

[Subject index](INDEX.md) · [Previous](asyncio-future-class.md) · [Continue](asyncio-future-exception-to-asyncio-future-get-loop.md) · [Owning module, declaration or section: asyncio.Future](asyncio-future-class.md) · [Owning module, declaration or section: Future Object](asyncio-future-class.md)
