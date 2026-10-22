# Python 3.11.0 alpha 1 / c api / type

[bpo-44263](https://bugs.python.org/issue?@action=redirect&bpo=44263): The [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) function now signals an error whenever a type carries the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag yet provides no traverse function ([`PyTypeObject.tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse)). Victor Stinner wrote the patch.

[bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035): Introduce a fresh [`PyType_GetName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetName) function returning a type's short name.

[bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035): Introduce a fresh [`PyType_GetQualName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetQualName) function returning a type's qualified name.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
