# Python 3.9.0 beta 1 / library / asyncio task

[bpo-40607](https://bugs.python.org/issue?@action=redirect&bpo=40607): Should an error arise during cancellation, [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) now re-raises that exception when it cancels a task on timeout. Roman Skurikhin wrote the patch.

[bpo-31033](https://bugs.python.org/issue?@action=redirect&bpo=31033): On cancellation of an [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task), the exception traceback now chains the whole way back to the point where the task was first interrupted.

[bpo-40559](https://bugs.python.org/issue?@action=redirect&bpo=40559): Plug a potential memory leak found in the C implementation of [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
