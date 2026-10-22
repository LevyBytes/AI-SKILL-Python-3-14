# Python 3.9.0 alpha 4 / c api / allocation

[bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542): Inside the limited C API, `PyObject_INIT()` and `PyObject_INIT_VAR()` now stand as aliases for [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) and [`PyObject_InitVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_InitVar), keeping their implementation opaque. This stops implementation details from leaking into the limited C API. The following functions are excluded from the limited C API: `_Py_NewReference()`, `_Py_ForgetReference()`, `_PyTraceMalloc_NewReference()` and `_Py_GetRefTotal()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
