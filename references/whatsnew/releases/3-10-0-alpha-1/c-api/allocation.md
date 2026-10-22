# Python 3.10.0 alpha 1 / c api / allocation

[bpo-40989](https://bugs.python.org/issue?@action=redirect&bpo=40989): The [`PyObject_INIT()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_INIT) and [`PyObject_INIT_VAR()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_INIT_VAR) macros are now simply aliases for the [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) and [`PyObject_InitVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_InitVar) functions respectively.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
