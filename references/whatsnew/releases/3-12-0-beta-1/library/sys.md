# Python 3.12.0 beta 1 / library / sys

[gh-103176](https://github.com/python/cpython/issues/103176): [`sys._current_exceptions()`](https://docs.python.org/3.14/library/sys.html#sys._current_exceptions) now hands back a mapping that ties each thread-id to an exception instance rather than to a `(typ, exc, tb)` tuple.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
