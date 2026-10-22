# asyncio.task: `create_task()`

create_task(*coro*, ***, *name=None*, *context=None*, *eager_start=None*, ***kwargs*)

Add a task to this particular task group. Its signature lines up with that of `asyncio.create_task()`. Should the task group not be active (for instance, not entered yet, already done, or partway through shutting down), the supplied `coro` gets closed.

Changed in version 3.13: When the task group is inactive, the supplied coroutine is now closed.

Changed in version 3.14: Passes on all *kwargs* to [`loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task)

Example:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

```

By means of the `async with` statement, execution holds until every task in the group has completed. During that wait, additional tasks can still be appended to the group (for instance, by handing `tg` to one of the coroutines and invoking `tg.create_task()` from inside it). After the final task completes and the `async with` block is left, the group accepts no further tasks.

As soon as any of the group's tasks first fails with some exception apart from [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError), the group's other tasks get cancelled. From then on no additional tasks may be added to the group. At that moment, provided the body of the `async with` statement is still running (that is, [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) has not yet been invoked), the task that directly holds the `async with` statement is cancelled too. That resulting `asyncio.CancelledError` will break into an `await`, yet it won't escape past the surrounding `async with` statement.

After every task has wrapped up, should any of them have failed with an exception other than [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError), those exceptions get bundled together within an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) or [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) (whichever fits; consult their documentation), which is then raised.

A pair of base exceptions get special handling: When any task fails with [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) or [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), the task group still goes ahead and cancels the remaining tasks and awaits them, but afterward the original `KeyboardInterrupt` or `SystemExit` is re-raised rather than [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) or [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup).

Should the body of the `async with` statement leave with an exception (meaning [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) is called with an exception set), the handling matches the case of a task having failed: the leftover tasks get cancelled and then awaited, while non-cancellation exceptions are gathered into an exception group and raised. Unless it happens to be [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError), the exception handed to `__aexit__()` is folded into the exception group as well. That same special treatment applies to [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) and [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) just as in the paragraph before.

Task groups take care not to confuse the internal cancellation they use to “wake up” their [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) with cancellation requests aimed at the task they run in that come from elsewhere. Specifically, when one task group sits syntactically inside another, and each hits an exception in one of its child tasks at the same time, the inner task group handles its exceptions first, after which the outer task group gets a further cancellation and handles its own exceptions.

Where a task group faces external cancellation while also having to raise an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup), it invokes the parent task's `cancel()` method. Doing so guarantees that a [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) gets raised at the following [`await`](https://docs.python.org/3.14/reference/expressions.html#await), keeping the cancellation from being lost.

The cancellation count that `asyncio.Task.cancelling()` reports is kept intact by task groups.

Changed in version 3.13: Better treatment of internal and external cancellations occurring at once, plus accurate retention of cancellation counts.

[Subject index](INDEX.md) · [Previous](asyncio-taskgroup-class.md) · [Continue](terminating-a-task-group.md) · [Owning module, declaration or section: asyncio.TaskGroup](asyncio-taskgroup-class.md) · [Owning module, declaration or section: Task groups](asyncio-taskgroup-class.md)
