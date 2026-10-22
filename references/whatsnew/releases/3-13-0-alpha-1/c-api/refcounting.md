# Python 3.13.0 alpha 1 / c api / refcounting

[gh-105387](https://github.com/python/cpython/issues/105387): Under the limited C API version 3.12, the [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) and [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) functions now take the form of opaque function calls so implementation details stay hidden. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
