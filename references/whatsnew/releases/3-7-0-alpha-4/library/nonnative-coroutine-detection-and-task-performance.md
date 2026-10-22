# Python 3.7.0 alpha 4 / library / speed up asyncio iscoroutine loop create task coroutines not native instance async

[bpo-32357](https://bugs.python.org/issue?@action=redirect&bpo=32357): Speed up asyncio.iscoroutine() and loop.create_task() for coroutines that are not native (for instance, async/await compiled through Cython). "loop.create_task(python_coroutine)" once ran 20% faster than "loop.create_task(cython_coroutine)". These days the latter matches that speed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
