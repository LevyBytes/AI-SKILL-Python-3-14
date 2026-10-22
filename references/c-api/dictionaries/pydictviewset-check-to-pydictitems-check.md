# Dictionary View Objects

### Dictionary View Objects

 int PyDictViewSet_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yield true when *op* is a set view belonging to a dictionary. At present this matches PyDictKeys_Check(op) || PyDictItems_Check(op). The function never fails.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictKeys_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object representing a view of a dictionary's keys. Over in Python, it is the type that [`dict.keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys) hands back.

 int PyDictKeys_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yield true when *op* is an instance of a keys view of a dictionary. The function never fails.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictValues_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object representing a view of a dictionary's values. Over in Python, it is the type that [`dict.values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values) hands back.

 int PyDictValues_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yield true when *op* is an instance of a values view of a dictionary. The function never fails.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictItems_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object representing a view of a dictionary's items. Over in Python, it is the type that [`dict.items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) hands back.

 int PyDictItems_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yield true when *op* is an instance of an items view of a dictionary. The function never fails.

[Subject index](INDEX.md) · [Previous source contract](pydict-watchevent.md) · [Following source contract](pyodict-type-to-pyodict-delitem.md)
