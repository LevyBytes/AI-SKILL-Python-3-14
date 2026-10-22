# Barrier: `asyncio.Barrier`

### Barrier

 *class *asyncio.Barrier(*parties*)

A barrier object. Carries no thread safety.

A barrier is a basic synchronization primitive that lets execution stay blocked until *parties* tasks are all waiting on it. Tasks wait through the `wait()` method and remain blocked right up to the moment the stated count of tasks are all parked at `wait()`. From that instant, every waiting task unblocks together.

You can use [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) in place of awaiting `wait()`.

The barrier may be put to use again as many times as you like.

Example:

```python
async def example_barrier():
   # barrier with 3 parties
   b = asyncio.Barrier(3)

   # create 2 new waiting tasks
   asyncio.create_task(b.wait())
   asyncio.create_task(b.wait())

   await asyncio.sleep(0)
   print(b)

   # The third .wait() call passes the barrier
   await b.wait()
   print(b)
   print("barrier passed")

   await asyncio.sleep(0)
   print(b)

asyncio.run(example_barrier())

```

Running this example produces:

```python
<asyncio.locks.Barrier object at 0x... [filling, waiters:2/3]>
<asyncio.locks.Barrier object at 0x... [draining, waiters:0/3]>
barrier passed
<asyncio.locks.Barrier object at 0x... [filling, waiters:0/3]>

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](asyncio-boundedsemaphore-class.md) · [Continue](asyncio-barrier-wait-to-asyncio-barrier-abort.md)
