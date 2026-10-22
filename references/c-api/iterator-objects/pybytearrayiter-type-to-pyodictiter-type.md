# Other Iterator Objects

### Other Iterator Objects

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyByteArrayIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyBytesIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyListIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyListRevIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PySetIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyTupleIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyRangeIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyLongRangeIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictIterKey_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictRevIterKey_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictIterValue_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictRevIterValue_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictIterItem_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictRevIterItem_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyODictIter_Type

The type objects for iterators of assorted built-in objects.

Refrain from instantiating these on your own; instead route through [`PyObject_GetIter()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetIter).

Bear in mind that nothing promises a particular built-in type will employ a particular iterator type. As an illustration, looping over [`range`](https://docs.python.org/3.14/library/stdtypes.html#range) picks between two iterator types according to the range's size. Additional types could adopt a comparable approach down the line, with no notice given.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyseqiter-type-to-pycalliter-new.md) · [Previous source contract](builtin-iterator-types.md) · [Following source contract](../object-life-cycle/object-life-cycle.md)
