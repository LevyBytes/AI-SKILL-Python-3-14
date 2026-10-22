# Python 3.8.0 alpha 1 / library / asyncio task

[bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751): Whenever a task is cancelled because of a timeout, [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) now holds until that cancellation finishes.

[bpo-34270](https://bugs.python.org/issue?@action=redirect&bpo=34270): Every default asyncio task object now carries a name, which two fresh methods can read or change ([`get_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.get_name) and [`set_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.set_name)); that name also shows up in the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) output. You may supply a starting name through the new `name` keyword argument on [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) or via the event loop's `create_task()` method. When no starting name is provided, the standard Task implementation derives a label such as `Task-1` from a monotonic counter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
