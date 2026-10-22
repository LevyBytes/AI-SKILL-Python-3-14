# Display the current date with call_later()

### Display the current date with call_later()

Here a callback prints the current date once per second. By way of the `loop.call_later()` method the callback re-arms itself five seconds later, and finally halts the event loop:

```python
import asyncio
import datetime as dt

def display_date(end_time, loop):
    print(dt.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

loop = asyncio.new_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()

```

See also

A similar [current date](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-sleep) example created with a coroutine and the [`run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) function.

[Subject index](INDEX.md) · [Previous](hello-world-with-call-soon.md) · [Continue](watch-a-file-descriptor-for-read-events.md)
