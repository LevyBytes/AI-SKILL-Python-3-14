# Python 3.14.0 alpha 5 / library / asyncio eventloop

[gh-128308](https://github.com/python/cpython/issues/128308): Accept the *name* keyword argument for eager tasks across [`asyncio.loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task), [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) and [`asyncio.TaskGroup.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup.create_task) by forwarding every *kwargs* to whatever task factory was registered through [`asyncio.loop.set_task_factory()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
