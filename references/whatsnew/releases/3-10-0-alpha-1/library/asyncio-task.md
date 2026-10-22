# Python 3.10.0 alpha 1 / library / asyncio task

[bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751): On cancelling a task because of a timeout, [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) will now hold off until the cancellation finishes even when *timeout* is <= 0, mirroring its behavior with positive timeouts.

[bpo-37658](https://bugs.python.org/issue?@action=redirect&bpo=37658): [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) now copes correctly with races between its own cancellation and completion of the wrapped awaitable.

[bpo-32309](https://bugs.python.org/issue?@action=redirect&bpo=32309): Introduced a fresh [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine), [`asyncio.to_thread()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.to_thread). Its main job is to run IO-bound functions on a separate thread so the event loop does not block, and it effectively serves as a high-level wrapper over [`run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) that accepts keyword arguments directly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
