# Python 3.12.0 alpha 2 / library / traceback

[gh-98878](https://github.com/python/cpython/issues/98878): Draw on the frame-bound builtins while proposing a name in [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback), avoiding a crash whenever `__builtins__` is something other than a dict.

[gh-98744](https://github.com/python/cpython/issues/98744): Stop [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) from crashing as it fetches the byte-offset for certain source files holding particular unicode characters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
