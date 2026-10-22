# Timeouts: `asyncio.wait_for()`

*async *asyncio.wait_for(*aw*, *timeout*)

Wait for the *aw* awaitable to complete with a timeout.

When *aw* happens to be a coroutine, it gets scheduled as a Task on its own.

*timeout* may be either `None` or a float or int count of seconds to wait. Passing `None` for *timeout* blocks until the future is finished.

Should a timeout fire, the task is cancelled and a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) is raised.

Wrap the task in `shield()` if you want to keep it from being `cancellation`.

Because the function waits for the future to finish cancelling, the overall wait can run longer than the *timeout*. Any exception raised while cancelling is propagated.

Cancelling the wait also cancels the future *aw*.

Example:

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!

```

Changed in version 3.7: Once *aw* is cancelled because of a timeout, `wait_for` holds until *aw* finishes cancelling. Earlier releases raised [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) right away.

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Raises [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) instead of [`asyncio.TimeoutError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.TimeoutError).

[Subject index](INDEX.md) · [Previous](asyncio-timeout-class-to-asyncio-timeout-at.md) · [Continue](asyncio-wait.md) · [Owning module, declaration or section: asyncio.Timeout](asyncio-timeout-class-to-asyncio-timeout-at.md) · [Owning module, declaration or section: Timeouts](asyncio-timeout.md)
