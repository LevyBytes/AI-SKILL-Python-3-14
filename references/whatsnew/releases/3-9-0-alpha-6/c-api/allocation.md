# Python 3.9.0 alpha 6 / c api / allocation

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): So as to conceal implementation details, the `PyObject_NEW()` macro is now just an alias for the [`PyObject_New()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New) macro, and `PyObject_NEW_VAR()` becomes an alias for the [`PyObject_NewVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) macro. Neither reaches straight into the [`PyTypeObject.tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) member anymore.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
