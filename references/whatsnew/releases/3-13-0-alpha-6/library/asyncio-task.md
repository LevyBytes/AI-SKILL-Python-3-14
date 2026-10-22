# Python 3.13.0 alpha 6 / library / asyncio task

[bpo-33533](https://bugs.python.org/issue?@action=redirect&bpo=33533): [`asyncio.as_completed()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.as_completed) now hands back an object that doubles as both an asynchronous iterator and an ordinary one. With the fresh async-iteration style it becomes simpler to line up each earlier task against the result it produced. That brings it nearer to how [`concurrent.futures.as_completed()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.as_completed) iterates. Justin Arthur supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
