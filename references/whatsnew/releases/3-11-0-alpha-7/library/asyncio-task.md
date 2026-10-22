# Python 3.11.0 alpha 7 / library / asyncio task

[bpo-47167](https://bugs.python.org/issue?@action=redirect&bpo=47167): Make it possible to override a future-compliance check inside [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).

[bpo-46995](https://bugs.python.org/issue?@action=redirect&bpo=46995): For third-party task implementations, a missing [`asyncio.Task.set_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.set_name) is now deprecated, with the plan being to require it in Python 3.13.

[bpo-46994](https://bugs.python.org/issue?@action=redirect&bpo=46994): Take an explicit contextvars.Context in [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) and [`asyncio.loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task).

[bpo-464471](https://bugs.python.org/issue?@action=redirect&bpo=464471): The [`asyncio.timeout()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.timeout) and [`asyncio.timeout_at()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.timeout_at) context managers are now available. Tin Tvrtković and Andrew Svetlov supplied the patch.

[bpo-34790](https://bugs.python.org/issue?@action=redirect&bpo=34790): Stop allowing coroutine objects to be handed to [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
