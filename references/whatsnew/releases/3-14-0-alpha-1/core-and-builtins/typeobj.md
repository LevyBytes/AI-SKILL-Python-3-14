# Python 3.14.0 alpha 1 / core and builtins / typeobj

[gh-122527](https://github.com/python/cpython/issues/122527): Stop the crash that happened when a `PyStructSequence` got deallocated after the GC had cleared its type's dictionary. The type's [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) now takes into account non-sequence fields left out of the sequence's [`Py_SIZE`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
