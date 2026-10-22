# Running tasks concurrently

### Running tasks concurrently

 *awaitable *asyncio.gather(**aws*, *return_exceptions=False*)

Run awaitable objects in the *aws* sequence *concurrently*.

Whenever some awaitable inside *aws* happens to be a coroutine, it gets scheduled as a Task automatically.

Provided that every awaitable finishes successfully, the outcome is a combined list of the values returned. The sequence of those result values matches the sequence of awaitables within *aws*.

When *return_exceptions* is `False` (default), the very first exception raised propagates without delay to the task awaiting on `gather()`. The remaining awaitables in the *aws* sequence **won’t be cancelled** and will keep running.

When *return_exceptions* is `True`, exceptions get handled just like successful results, being collected together into the result list.

Whenever `gather()` is *cancelled*, each of the submitted awaitables (those still unfinished) is *cancelled* as well.

Should any Task or Future within the *aws* sequence be *cancelled*, it is handled as though it had raised [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) – here the `gather()` call itself is **not** cancelled. The point of this is to stop one submitted Task/Future's cancellation from triggering the cancellation of other Tasks/Futures.

Note

For concurrently creating and running tasks and then awaiting their completion, `asyncio.TaskGroup` serves as a fresh alternative. When scheduling nested subtasks, *TaskGroup* offers safety guarantees beyond those of *gather*: should a task (or a subtask, namely a task that another task scheduled) raise an exception, *TaskGroup* cancels the rest of the scheduled tasks whereas *gather* does not.

Example:

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]

```

Note

When *return_exceptions* is false, calling gather() to cancel after it has already been flagged done will not cancel any submitted awaitables. As an example, gather may be flagged done once it has propagated an exception out to the caller; consequently, invoking `gather.cancel()` once you have caught an exception (one raised by an awaitable) coming from gather will not cancel any of the other awaitables.

Changed in version 3.7: Cancelling the *gather* itself now propagates that cancellation no matter what *return_exceptions* is set to.

Changed in version 3.10: Removed the *loop* parameter.

Deprecated since version 3.10: A deprecation warning gets raised whenever positional arguments are absent, or some of them aren't Future-like objects, while no event loop is currently running.

[Subject index](INDEX.md) · [Previous](asyncio-sleep.md) · [Continue](eager-task-factory-creation.md)
