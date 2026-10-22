# Hello World with call_soon()

### Hello World with call_soon()

This example schedules a callback with the `loop.call_soon()` method. That callback prints `"Hello World"` and afterward halts the event loop:

```python
import asyncio

def hello_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')
    loop.stop()

loop = asyncio.new_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()

```

See also

A similar [Hello World](https://docs.python.org/3.14/library/asyncio-task.html#coroutine) example created with a coroutine and the [`run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) function.

[Subject index](INDEX.md) · [Previous](examples.md) · [Continue](display-the-current-date-with-call-later.md)
