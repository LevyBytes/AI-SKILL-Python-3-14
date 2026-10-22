# Timeouts: Timeout cancellation and TimeoutError handling

Should `long_running_task` run past the 10-second mark before finishing, the context manager cancels the active task and absorbs the [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) that follows, converting it into a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) that your code may catch and handle.

Note

It is the `asyncio.timeout()` context manager that performs the conversion of [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) into a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError). Because of this, you can only catch the `TimeoutError` from *outside* the context manager.

Example of catching [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError):

```python
async def main():
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")

```

You can move the deadline of the context manager returned by `asyncio.timeout()` to a new value and also query it.

[Subject index](INDEX.md) · [Continue](asyncio-timeout-class-to-asyncio-timeout-at.md) · [Owning module, declaration or section: Timeouts](asyncio-timeout.md) · [Owning module, declaration or section: asyncio.timeout](asyncio-timeout.md) · [Preceding source contract and version conditions](asyncio-timeout.md)
