# Python 3.10.0 alpha 3 / c api / list

[bpo-30459](https://bugs.python.org/issue?@action=redirect&bpo=30459): The [`PyList_SET_ITEM()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_SET_ITEM), [`PyTuple_SET_ITEM()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SET_ITEM) and [`PyCell_SET()`](https://docs.python.org/3.14/c-api/cell.html#c.PyCell_SET) macros are no longer permitted as an l-value or r-value. To illustrate, `x = PyList_SET_ITEM(a, b, c)` and `PyList_SET_ITEM(a, b, c) = x` now break with a compiler error. This guards against defects such as the `if (PyList_SET_ITEM (a, b, c) < 0) ...` test. Zackery Spytz and Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
