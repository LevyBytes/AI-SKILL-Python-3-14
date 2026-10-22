# Running and stopping the loop

### Running and stopping the loop

 loop.run_until_complete(*future*)

Run until the *future* (an instance of [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future)) has completed.

When the argument is a [coroutine object](https://docs.python.org/3.14/library/asyncio-task.html#coroutine), it is automatically arranged to run as an [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).

Return the Future’s result or raise its exception.

 loop.run_forever()

Run the event loop until `stop()` is called.

Should `stop()` be invoked before `run_forever()` itself runs, the loop polls the I/O selector a single time using a zero timeout, executes every callback queued in response to I/O events (together with those already queued), and then quits.

Should `stop()` be invoked while `run_forever()` is active, the loop finishes the current set of callbacks and then quits. Be aware that any new callbacks queued by callbacks won’t run here; rather, they will execute on the next `run_forever()` or `run_until_complete()` call.

 loop.stop()

Stop the event loop.

 loop.is_running()

Return `True` if the event loop is currently running.

 loop.is_closed()

Return `True` if the event loop was closed.

 loop.close()

Close the event loop.

While this function executes, the loop must be stopped. Whatever callbacks remain pending are thrown away.

Although this method empties every queue and shuts the executor down, it does not block until the executor completes.

The method is both idempotent and irreversible. Once the event loop has closed, no further methods may be invoked on it.

 *async *loop.shutdown_asyncgens()

Schedule all currently open [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) objects to close with an [`aclose()`](https://docs.python.org/3.14/reference/expressions.html#agen.aclose) call. Once this method runs, the event loop will warn whenever a fresh asynchronous generator is iterated. Rely on this to dependably wind down all queued asynchronous generators.

Bear in mind that calling this function is unnecessary whenever [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) is in play.

Example:

```python
try:
    loop.run_forever()
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

```

Added in version 3.6.

 *async *loop.shutdown_default_executor(*timeout=None*)

Schedule the default executor to close and wait until it has joined every thread inside the [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor). After this method runs, any attempt to use the default executor through `loop.run_in_executor()` will raise a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

How long (in [`float`](https://docs.python.org/3.14/library/functions.html#float) seconds) the executor gets to complete its joining is governed by the *timeout* parameter. The default of `None` grants the executor an unbounded stretch of time.

Should the *timeout* elapse, a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) is raised and the default executor stops without holding out for its threads to finish joining.

Note

Avoid invoking this method together with [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run), since that helper deals with default executor shutdown on its own.

Added in version 3.9.

Changed in version 3.12: Added the *timeout* parameter.

[Subject index](INDEX.md) · [Previous](event-loop-methods.md) · [Continue](loop-call-soon-to-loop-call-soon-threadsafe.md)
