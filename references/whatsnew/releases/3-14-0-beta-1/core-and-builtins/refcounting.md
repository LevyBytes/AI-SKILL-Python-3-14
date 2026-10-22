# Python 3.14.0 beta 1 / core and builtins / refcounting

[gh-124715](https://github.com/python/cpython/issues/124715): Stack overflows during a [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) call are now prevented. Because the protection now lives within the `Py_DECREF()` macro itself, third-party extension objects no longer have to rely on the "trashcan" mechanism.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
