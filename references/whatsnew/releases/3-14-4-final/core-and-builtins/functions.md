# Python 3.14.4 final / core and builtins / functions

[gh-146056](https://github.com/python/cpython/issues/146056): Repairs [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) when lists and tuples hold `NULL`s.

[gh-145779](https://github.com/python/cpython/issues/145779): Better scaling for [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) plus [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) calls within the free-threaded build, achieved by skipping the descriptor `__get__` call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
