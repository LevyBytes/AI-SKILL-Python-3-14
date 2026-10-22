# Task lifetime support

### Task lifetime support

For a custom task type to stay discoverable through [`asyncio.all_tasks()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.all_tasks) and [`asyncio.current_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.current_task), it must invoke the routines below:

 asyncio._register_task(*task*)

Records a fresh *task* as being managed by *asyncio*.

Invoke it from within a task constructor.

 asyncio._unregister_task(*task*)

Removes a *task* from the internal bookkeeping of *asyncio*.

You should invoke it as a task nears completion.

 asyncio._enter_task(*loop*, *task*)

Makes the supplied *task* argument the active current task.

Invoke it immediately before running a slice of the wrapped *coroutine* (either [`coroutine.send()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.send) or [`coroutine.throw()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.throw)).

 asyncio._leave_task(*loop*, *task*)

Reverts the current task away from *task*, restoring it to `None`.

Invoke it right after a [`coroutine.send()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.send) or [`coroutine.throw()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.throw) call returns.

[Subject index](INDEX.md) · [Previous](future-init-to-task-init.md) · [Continue](../asyncio-future/futures.md)
