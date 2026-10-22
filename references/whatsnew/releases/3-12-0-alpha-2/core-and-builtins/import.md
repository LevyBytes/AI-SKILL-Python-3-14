# Python 3.12.0 alpha 2 / core and builtins / import

[gh-81057](https://github.com/python/cpython/issues/81057): The docs state plainly that [`PyImport_Inittab`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_Inittab), [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab), and [`PyImport_ExtendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ExtendInittab) must not be used once [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) has run. That rule is now enforced for the latter two functions. On top of that, the runtime keeps an internal copy of `PyImport_Inittab` to defend against modification.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
