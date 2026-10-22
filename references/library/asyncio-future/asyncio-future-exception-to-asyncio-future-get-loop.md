# asyncio.future: `exception()`, `get_loop()`

exception()

Hand back whichever exception was placed on this Future.

That exception (or `None` when none was attached) comes back only once the Future is *done*.

When the Future sits in the *cancelled* state, this method throws a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception.

When the Future has not reached *done* yet, this method throws an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) exception.

 get_loop()

Hand back the event loop that this Future object is tied to.

Added in version 3.7.

The snippet below builds a Future object, then creates and queues an asynchronous Task that fills in the Future's result, and finally blocks until the Future holds a result:

```python
async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)

asyncio.run(main())

```

Important

The Future object was built to resemble [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future), yet the two part ways in several places:

- in contrast to asyncio Futures, an instance of [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) can never be awaited.

- neither `asyncio.Future.result()` nor `asyncio.Future.exception()` takes the *timeout* argument.

- `asyncio.Future.result()` together with `asyncio.Future.exception()` throw an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) exception whenever the Future has not reached *done*.

- Callbacks attached through `asyncio.Future.add_done_callback()` do not fire on the spot; they instead get queued by way of [`loop.call_soon()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon).

- an asyncio Future does not work with the [`concurrent.futures.wait()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.wait) or [`concurrent.futures.as_completed()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.as_completed) functions.

- `asyncio.Future.cancel()` will take an optional `msg` argument, whereas [`concurrent.futures.Future.cancel()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future.cancel) will not.

[Subject index](INDEX.md) · [Previous](asyncio-future-result-to-asyncio-future-cancel.md) · [Continue](../asyncio-graph/asyncio-print-call-graph-to-futurecallgraph.md) · [Owning module, declaration or section: asyncio.Future](asyncio-future-class.md) · [Owning module, declaration or section: Future Object](asyncio-future-class.md)
