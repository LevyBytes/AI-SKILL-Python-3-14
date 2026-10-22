# Python 3.12.0 alpha 7 / core and builtins / exceptions

[gh-102755](https://github.com/python/cpython/issues/102755): Introduce [`PyErr_DisplayException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_DisplayException), which accepts only an exception instance, as a replacement for the legacy `PyErr_Display()` that wanted the `(typ, exc, tb)` triplet.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
