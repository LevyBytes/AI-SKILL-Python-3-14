# Python 3.14.0 beta 3 / c api / repair py return none py return true py return false macros within limited c api

[gh-134989](https://github.com/python/cpython/issues/134989): Repair the `Py_RETURN_NONE`, `Py_RETURN_TRUE` and `Py_RETURN_FALSE` macros within the limited C API 3.11 and earlier: stop regarding `Py_None`, `Py_True` and `Py_False` as immortal. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
