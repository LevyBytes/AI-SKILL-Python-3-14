# Python 3.9.0 alpha 6 / c api / type

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): To keep implementation details hidden, [`PyType_HasFeature()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_HasFeature) now invariably routes through [`PyType_GetFlags()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetFlags). Up to now it reached straight into the [`PyTypeObject.tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) member whenever the limited C API wasn't in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
