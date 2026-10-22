# Python 3.7.0 beta 5 / library / asyncio task

[bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751): Upon cancelling a task because of a timeout, [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) will from now on hold until the cancellation finishes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
