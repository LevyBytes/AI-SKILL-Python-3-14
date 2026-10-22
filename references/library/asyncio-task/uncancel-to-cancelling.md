# Task cancellation state and cancellation counts

A Task counts as *cancelled* once two things have happened: a `cancel()` call asked for cancellation, and the coroutine it wraps let the injected [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception bubble up.

`uncancel()`

Lowers, by one, the tally of cancellation requests recorded against this Task.

The value handed back is however many cancellation requests are still outstanding.

Be aware that after a cancelled task has finished running, any later invocation of `uncancel()` accomplishes nothing.

Added in version 3.11.

asyncio relies on this method internally, and it generally isn't something application code reaches for. The point is that an uncancelled Task lets structured-concurrency constructs — Task groups, `asyncio.timeout()` and the like — keep going, which confines a cancellation to whichever structured block it belongs in. As an illustration:

```python
async def make_request_with_timeout():
    try:
        async with asyncio.timeout(1):
            # Structured block affected by the timeout:
            await make_request()
            await make_another_request()
    except TimeoutError:
        log("There was a timeout")
    # Outer code not affected by the timeout:
    await unrelated_code()

```

Even though the timeout may cancel the block holding `make_request()` and `make_another_request()`, the call to `unrelated_code()` is meant to carry on regardless of that timeout. `uncancel()` is what makes this work, and `TaskGroup` context managers lean on `uncancel()` the same way.

Should application code choose, for whatever reason, to swallow cancellation by trapping [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError), it must invoke this method afterward so the cancellation state is cleared.

Bringing the cancellation count down to zero triggers a check inside this method: did an earlier `cancel()` schedule a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) to land in the task? When that throw is still pending, the scheduling is undone (the internal `_must_cancel` flag gets cleared).

Changed in version 3.13: Now withdraws any outstanding cancellation requests once the count hits zero.

`cancelling()`

Hands back how many cancellation requests are currently pending for this Task — that is, the count of `cancel()` invocations minus the count of `uncancel()` invocations.

Keep in mind that a positive value here does not stop `cancelled()` from returning `False` while the Task is still mid-execution. The reason is that `uncancel()` can drive this figure back down, and if the requests reach zero the task may end up never being cancelled at all.

asyncio uses this method internally, and application code generally has no reason to call it. Consult `uncancel()` for the fuller picture.

Added in version 3.11.

[Subject index](INDEX.md)
