# Sleeping

### Sleeping

 *async *asyncio.sleep(*delay*, *result=None*)

Block for *delay* seconds.

Whenever *result* is supplied, that value is handed back to the caller once the coroutine finishes.

`sleep()` always suspends the current task, allowing other tasks to run.

Giving the delay a value of 0 offers a streamlined route that lets other tasks proceed. Long-running functions can take advantage of this to keep from holding up the event loop for their whole call duration.

Example of coroutine displaying the current date every second for 5 seconds:

```python
import asyncio
import datetime as dt

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(dt.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())

```

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.13: Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if *delay* is [`nan`](https://docs.python.org/3.14/library/math.html#math.nan).

[Subject index](INDEX.md) · [Previous](terminating-a-task-group.md) · [Continue](running-tasks-concurrently.md)
