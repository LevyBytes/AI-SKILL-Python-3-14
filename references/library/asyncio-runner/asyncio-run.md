# Running an asyncio Program

### Running an asyncio Program

 asyncio.run(*coro*, ***, *debug=None*, *loop_factory=None*)

Execute *coro* in an asyncio event loop and return the result.

The argument can be any awaitable object.

This function executes the awaitable while handling the asyncio event loop on your behalf, *finalizing asynchronous generators*, and shutting the executor down.

You cannot invoke this function while a different asyncio event loop is already running on the same thread.

With *debug* set to `True`, the event loop runs in debug mode. Passing `False` turns debug mode off outright, while `None` leaves the global [Debug Mode](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-debug-mode) settings in charge.

When *loop_factory* is anything but `None`, it builds the new event loop; failing that, [`asyncio.new_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.new_event_loop) does the job. The loop gets closed once finished. Treat this function as the principal entry point for asyncio programs and, ideally, call it just once. Configuring the event loop through *loop_factory* rather than policies is the recommended route. Hand it [`asyncio.EventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.EventLoop) and you can run asyncio with the policy system out of the picture.

A shutdown window of 5 minutes is allotted to the executor. Should the executor still be unfinished when that window closes, a warning fires and the executor is shut down anyway.

Example:

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())

```

Added in version 3.7.

Changed in version 3.9: Updated to use [`loop.shutdown_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor).

Changed in version 3.10: The default for *debug* became `None`, so the global debug mode settings are honored.

Changed in version 3.12: Added *loop_factory* parameter.

Changed in version 3.14: *coro* can be any awaitable object.

Note

Deprecation has come to the `asyncio` policy system, which Python 3.16 will drop; once that lands, configuring the event loop will require an explicit *loop_factory*.

[Subject index](INDEX.md) · [Previous](runners.md) · [Continue](asyncio-runner-class.md)
