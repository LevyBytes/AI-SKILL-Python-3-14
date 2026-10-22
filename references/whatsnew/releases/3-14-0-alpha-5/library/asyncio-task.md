# Python 3.14.0 alpha 5 / library / asyncio task

[gh-128550](https://github.com/python/cpython/issues/128550): Drop a faulty optimization for eager tasks inside [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) that had caused some cancellations to slip through.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
