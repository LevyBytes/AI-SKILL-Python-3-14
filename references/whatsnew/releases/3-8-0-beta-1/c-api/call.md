# Python 3.8.0 beta 1 / c api / call

[bpo-37107](https://bugs.python.org/issue?@action=redirect&bpo=37107): Reworks [`PyObject_CallMethodObjArgs()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethodObjArgs) and `_PyObject_CallMethodIdObjArgs` to employ `_PyObject_GetMethod`, sidestepping the creation of a bound method object in plenty of situations. Michael J. Sullivan supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
