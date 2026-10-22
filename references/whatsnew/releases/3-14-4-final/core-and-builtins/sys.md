# Python 3.14.4 final / core and builtins / sys

[gh-146041](https://github.com/python/cpython/issues/146041): Removes a free-threading scaling bottleneck affecting [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern) plus [`PyObject_SetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttr); the interpreter-wide lock is now skipped whenever the string is already interned along with being immortalized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
