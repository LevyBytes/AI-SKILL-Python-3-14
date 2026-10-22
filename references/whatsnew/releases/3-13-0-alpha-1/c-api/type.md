# Python 3.13.0 alpha 1 / c api / type

[gh-105227](https://github.com/python/cpython/issues/105227): The fresh [`PyType_GetDict()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetDict) hands you the dictionary for a given type object that `cls.__dict__` would normally expose. Usually relying on [`tp_dict`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dict) is enough, but `tp_dict` is now perpetually `NULL` for the static builtin types. In those cases `PyType_GetDict()` returns the right dict object.

[gh-103968](https://github.com/python/cpython/issues/103968): Metaclasses whose `tp_new` is `NULL` are now accepted by [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
