# Python 3.12.0 alpha 4 / library / contextlib

[gh-95882](https://github.com/python/cpython/issues/95882): Repair a 3.11 regression in [`asynccontextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.asynccontextmanager) that made it propagate exceptions with the wrong tracebacks, and likewise repair a 3.11 regression in [`contextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager) that made it propagate exceptions with the wrong tracebacks for [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
