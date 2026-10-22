# Handling Keyboard Interruption

### Handling Keyboard Interruption

Added in version 3.11.

By default, when Ctrl-C triggers [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT), a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception fires in the main thread. That arrangement falls apart with [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), though, since it may break into asyncio's internals and leave the program unable to exit.

To mitigate this issue, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) handles [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) as follows:

1.

Ahead of running any user code, `asyncio.Runner.run()` puts a custom [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) handler in place, then takes it back out as it leaves the function.

2.

The `Runner` creates the main task for the passed coroutine for its execution.

3.

Once Ctrl-C raises [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT), the custom signal handler cancels the main task through a [`asyncio.Task.cancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel) call, which in turn raises [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) within that main task. The Python stack then unwinds, and you can lean on `try/except` and `try/finally` blocks to clean up resources. Following the main task's cancellation, `asyncio.Runner.run()` raises [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt).

4.

It's possible for a user to write a tight loop that [`asyncio.Task.cancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel) cannot break into; in that situation the next Ctrl-C after it raises [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) on the spot, leaving the main task uncancelled.

[Subject index](INDEX.md) · [Previous](asyncio-runner-run-to-asyncio-runner-get-loop.md)
