# Python 3.12.0 alpha 1 / c api / type

[gh-89546](https://github.com/python/cpython/issues/89546): [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass) and the other `PyType_From*` functions now confirm that the offsets along with the base class's [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) will fit inside the new class's `tp_basicsize`.

[bpo-45383](https://bugs.python.org/issue?@action=redirect&bpo=45383): Given the supplied bases, the [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec) API will now locate and apply an appropriate metaclass. Should a metaclass conflict arise, an error is raised.

[gh-91051](https://github.com/python/cpython/issues/91051): Add [`PyType_Watch()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Watch) and related APIs to allow callbacks on [`PyType_Modified()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Modified).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
