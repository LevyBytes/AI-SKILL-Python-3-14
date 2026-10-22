# Python 3.14.1 final / c api / object

[gh-140487](https://github.com/python/cpython/issues/140487): Correct [`Py_RETURN_NOTIMPLEMENTED`](https://docs.python.org/3.14/c-api/object.html#c.Py_RETURN_NOTIMPLEMENTED) under limited C API 3.11 and earlier: avoid treating `Py_NotImplemented` as immortal. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
