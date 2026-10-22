# Python 3.13.0 alpha 3 / c api / clear duplicate declarations out public c api

[gh-106560](https://github.com/python/cpython/issues/106560): Clear duplicate declarations out of the public C API. Now PyBool_Type, PyLong_Type and PySys_Audit() are each declared a single time. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
