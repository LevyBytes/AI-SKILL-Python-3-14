# Python 3.14.0 alpha 1 / core and builtins / long

[gh-121115](https://github.com/python/cpython/issues/121115): By default [`PyLong_AsNativeBytes()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsNativeBytes) no longer reaches for [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) methods. A new `Py_ASNATIVEBYTES_ALLOW_INDEX` flag re-enables that behavior.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
