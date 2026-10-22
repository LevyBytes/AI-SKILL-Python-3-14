# Python 3.12.0 beta 1 / library / asyncio task

[gh-104144](https://github.com/python/cpython/issues/104144): Make [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) more efficient with [`asyncio.eager_task_factory()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.eager_task_factory). Avoid scheduling a done callback when a TaskGroup task finishes eagerly.

[gh-104144](https://github.com/python/cpython/issues/104144): Make [`asyncio.gather()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather) more efficient with [`asyncio.eager_task_factory()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.eager_task_factory) so it finishes eagerly whenever every future completed eagerly. Skip scheduling done callbacks for the futures that finish eagerly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
