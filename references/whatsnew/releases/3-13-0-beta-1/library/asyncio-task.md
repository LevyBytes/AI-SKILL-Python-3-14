# Python 3.13.0 beta 1 / library / asyncio task

[gh-116720](https://github.com/python/cpython/issues/116720): Refines the conduct of [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) when an external cancellation coincides with an internal one. As an illustration, with two task groups nested and each hitting an exception in a child task at the same moment, the outer task group could previously misbehave because the inner group had swallowed its internal cancellation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
