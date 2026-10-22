# asyncio.runner: `asyncio.Runner`

### Runner context manager

 *class *asyncio.Runner(***, *debug=None*, *loop_factory=None*)

A context manager built to ease making *multiple* async function calls within one shared context.

There are times when a handful of top-level async functions ought to run within one shared [event loop](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop) and a single [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context).

A *debug* value of `True` makes the event loop run in debug mode, `False` shuts debug mode off deliberately, and `None` defers to whatever the global [Debug Mode](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-debug-mode) settings say.

You can supply *loop_factory* to take over how the loop is created. It falls to the *loop_factory* to mark the loop it builds as the current one. When *loop_factory* is `None`, the default path uses [`asyncio.new_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.new_event_loop) and installs it as the current event loop via [`asyncio.set_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.set_event_loop).

In essence, the earlier `asyncio.run()` example can be recast to lean on the runner:

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

with asyncio.Runner() as runner:
    runner.run(main())

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](asyncio-run.md) · [Continue](asyncio-runner-run-to-asyncio-runner-get-loop.md)
