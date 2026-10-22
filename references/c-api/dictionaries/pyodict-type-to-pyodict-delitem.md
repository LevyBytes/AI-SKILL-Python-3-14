# Ordered Dictionaries

### Ordered Dictionaries

From C, the Python C API exposes an interface to [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict). Dictionaries have kept insertion order by default ever since Python 3.7, which usually leaves these functions with scant purpose; favor `PyDict*` wherever you can.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyODict_Type

The type object that stands for ordered dictionaries. At the Python layer it is one and the same as [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict).

 int PyODict_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *od)

Yield true when *od* is an ordered dictionary object, or else an instance of some subtype of the [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) type. The function never fails.

 int PyODict_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *od)

Yield true when *od* is an ordered dictionary object yet not an instance of any subtype of the [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) type. The function never fails.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyODictKeys_Type

The ordered-dictionary counterpart of `PyDictKeys_Type`.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyODictValues_Type

The ordered-dictionary counterpart of `PyDictValues_Type`.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyODictItems_Type

The ordered-dictionary counterpart of `PyDictItems_Type`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyODict_New(void)

Give back a fresh empty ordered dictionary, or `NULL` if it fails.

This mirrors `PyDict_New()`.

 int PyODict_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *od, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

Place *value* into the ordered dictionary *od* under the key *key*. Give back `0` on success, or `-1` with an exception set when it fails.

This mirrors `PyDict_SetItem()`.

 int PyODict_DelItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *od, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

Drop the entry whose key is *key* from the ordered dictionary *od*. Give back `0` on success, or `-1` with an exception set when it fails.

This mirrors `PyDict_DelItem()`.

The following are [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) aliases pointing at `PyDict` APIs:

| `PyODict` | `PyDict` |
| --- | --- |
| PyODict_GetItem(od, key) | `PyDict_GetItem()` |
| PyODict_GetItemWithError(od, key) | `PyDict_GetItemWithError()` |
| PyODict_GetItemString(od, key) | `PyDict_GetItemString()` |
| PyODict_Contains(od, key) | `PyDict_Contains()` |
| PyODict_Size(od) | `PyDict_Size()` |
| PyODict_SIZE(od) | `PyDict_GET_SIZE()` |

[Subject index](INDEX.md) · [Previous source contract](pydictviewset-check-to-pydictitems-check.md)
