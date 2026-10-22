# Python 3.12.0 alpha 3 / library / unittest

[gh-98458](https://github.com/python/cpython/issues/98458): Stop the infinite loop in unittest that occurred when a self-referencing chained exception is raised.

[gh-99645](https://github.com/python/cpython/issues/99645): Correct a class-cleanup handling defect in [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase). `addClassCleanup()` now keeps distinct lists per `TestCase` subclass, while `doClassCleanups()` cleans up only the relevant class.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
