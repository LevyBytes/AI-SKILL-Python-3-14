# Timeouts: `asyncio.Timeout`, `reschedule()`, `asyncio.timeout_at()`

*class *asyncio.Timeout(*when*)

An [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers) for cancelling overdue coroutines.

Reach for `asyncio.timeout()` or `asyncio.timeout_at()` instead of constructing a `Timeout` object yourself.

`when` is meant to be an absolute moment, gauged against the event loop’s clock, at which the context should hit its timeout:

- When `when` is `None`, no timeout is ever raised.

- When `when < loop.time()`, the timeout fires during the event loop’s next pass.

>

 when() → [float](https://docs.python.org/3.14/library/functions.html#float) | [None](https://docs.python.org/3.14/library/constants.html#None)

Give back the deadline in effect, or `None` when no deadline has been set.

 reschedule(*when: [float](https://docs.python.org/3.14/library/functions.html#float) | [None](https://docs.python.org/3.14/library/constants.html#None)*)

Reschedule the timeout.

 expired() → [bool](https://docs.python.org/3.14/library/functions.html#bool)

Report whether the context manager has run past its deadline (expired).

Example:

```python
async def main():
    try:
        # We do not know the timeout when starting, so we pass ``None``.
        async with asyncio.timeout(None) as cm:
            # We know the timeout now, so we reschedule it.
            new_deadline = get_running_loop().time() + 10
            cm.reschedule(new_deadline)

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired():
        print("Looks like we haven't finished on time.")

```

Nesting timeout context managers together is safe to do.

Added in version 3.11.

 asyncio.timeout_at(*when*)

Like `asyncio.timeout()`, but here *when* is the absolute moment at which waiting stops, or `None`.

Example:

```python
async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    try:
        async with asyncio.timeout_at(deadline):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](timeouts.md) · [Continue](asyncio-wait-for.md) · [Owning module, declaration or section: Timeouts](asyncio-timeout.md)
