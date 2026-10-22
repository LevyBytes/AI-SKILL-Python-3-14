# Timeouts: `asyncio.timeout()`

### Timeouts

 asyncio.timeout(*delay*)

Hand back an [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers) usable for capping how long is spent waiting on something.

The *delay* may be either `None`, or a float/int count of seconds to wait. With *delay* set to `None`, no time limit applies at all; that can come in handy when the delay isn't known at the time the context manager gets created.

Whichever the case, the context manager may be rescheduled following its creation by means of `Timeout.reschedule()`.

Example:

```python
async def main():
    async with asyncio.timeout(10):
        await long_running_task()

```

[Subject index](INDEX.md) · [Previous](shielding-from-cancellation.md) · [Required continuation of the source contract](timeouts.md)
