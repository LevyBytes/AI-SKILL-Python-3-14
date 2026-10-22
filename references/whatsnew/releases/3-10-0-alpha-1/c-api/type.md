# Python 3.10.0 alpha 1 / c api / type

[bpo-41689](https://bugs.python.org/issue?@action=redirect&bpo=41689): When a type is built with [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), any signature placed in its `tp_doc` slot is now reachable through `__text_signature__`.

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): Undo the [`PyType_HasFeature()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_HasFeature) change: when the limited C API is absent it once more reads the [`PyTypeObject.tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) member directly, rather than invariably routing through [`PyType_GetFlags()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetFlags), which conceals implementation details.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
