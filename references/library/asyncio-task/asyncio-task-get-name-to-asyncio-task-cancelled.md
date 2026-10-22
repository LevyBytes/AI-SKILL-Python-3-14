# asyncio.task: `get_name()`, `set_name()`, `cancel()`, `cancelled()`

get_name()

Return the name of the Task.

If the Task never received an explicit name, the default asyncio Task implementation makes up a default name while the Task is being created.

Added in version 3.8.

 set_name(*value*)

Set the name of the Task.

Any object may serve as the *value* argument; it is afterward turned into a string.

Under the default Task implementation, that name turns up in the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) output of a task object.

Added in version 3.8.

 cancel(*msg=None*)

Request the Task to be cancelled.

Where the Task is already *done* or *cancelled*, return `False`; in every other case, return `True`.

What the method does is set up a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception to be thrown into the wrapped coroutine at the next turn of the event loop.

At that point the coroutine has an opportunity to tidy up or even refuse the request, swallowing the exception inside a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) … … `except CancelledError` … [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block. For that reason, in contrast to [`Future.cancel()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.cancel), `Task.cancel()` offers no guarantee that the Task ends up cancelled, though wholly suppressing cancellation is uncommon and is firmly discouraged. If the coroutine does choose to swallow the cancellation, it must also call `Task.uncancel()` on top of catching the exception.

Changed in version 3.9: Added the *msg* parameter.

Changed in version 3.11: The `msg` parameter now carries through from a cancelled task over to whoever awaits it.

The example that follows shows the way coroutines can step in on the cancellation request:

```python
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now

```

 cancelled()

Return `True` if the Task is *cancelled*.

[Subject index](INDEX.md) · [Previous](asyncio-task-done-to-asyncio-task-get-context.md) · [Owning module, declaration or section: asyncio.Task](asyncio-task-class.md) · [Owning module, declaration or section: Task object](asyncio-task-class.md)
