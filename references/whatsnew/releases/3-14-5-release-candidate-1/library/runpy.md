# Python 3.14.5 release candidate 1 / library / runpy

[gh-149117](https://github.com/python/cpython/issues/149117): Make [`runpy.run_module()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_module) and [`runpy.run_path()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_path) populate the [`name`](https://docs.python.org/3.14/library/exceptions.html#ImportError.name) attribute on any [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) they emit.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
