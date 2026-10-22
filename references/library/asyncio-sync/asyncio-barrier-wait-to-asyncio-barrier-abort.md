# Barrier: `wait()`, `reset()`, `abort()`

*async *wait()

Get past the barrier. Once every task taking part in the barrier has invoked this function, they all unblock at the same moment.

Should a waiting or blocked task at the barrier be cancelled, that task leaves the barrier while the barrier holds its current state. When the barrier's state is “filling”, the tally of waiting tasks drops by 1.

What comes back is an integer between 0 and `parties-1`, distinct per task. You can use it to single out one task for some particular housekeeping, e.g.:

```python
...
async with barrier as position:
   if position == 0:
      # Only one task prints this
      print('End of *draining phase*')

```

Should the barrier get broken or reset during a task's wait, this method may throw a `BrokenBarrierError` exception. It might throw a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) when a task is cancelled.

 *async *reset()

Put the barrier back into its standard, empty state. Whatever tasks are waiting on it will be handed the `BrokenBarrierError` exception.

When a barrier has broken, you may be better off discarding it and building a new one.

 *async *abort()

Drive the barrier into a broken state. This makes every present or later call to `wait()` fail with the `BrokenBarrierError`. Apply it, for instance, when one of the tasks has to bail out, so as to head off tasks waiting forever.

 parties

How many tasks are needed to get past the barrier.

 n_waiting

How many tasks are presently waiting inside the barrier as it fills.

 broken

A boolean that reads `True` when the barrier sits in the broken state.

[Subject index](INDEX.md) · [Previous](asyncio-barrier-class.md) · [Continue](asyncio-brokenbarriererror.md) · [Owning module, declaration or section: asyncio.Barrier](asyncio-barrier-class.md) · [Owning module, declaration or section: Barrier](asyncio-barrier-class.md)
