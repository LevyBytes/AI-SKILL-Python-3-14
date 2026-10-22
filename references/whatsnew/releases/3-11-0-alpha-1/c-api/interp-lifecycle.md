# Python 3.11.0 alpha 1 / c api / interp lifecycle

[bpo-44441](https://bugs.python.org/issue?@action=redirect&bpo=44441): On exit, [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain) now restores [`PyImport_Inittab`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_Inittab) to the value it started with. Calling [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab) or [`PyImport_ExtendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ExtendInittab) has to remain possible at every Python initialization. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
