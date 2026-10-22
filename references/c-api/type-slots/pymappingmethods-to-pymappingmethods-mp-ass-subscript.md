# Mapping Object Structures

### Mapping Object Structures

 type PyMappingMethods

Pointers to the functions an object relies on to carry out the mapping protocol are stored in this structure. Three members make it up:

 lenfunc PyMappingMethods.mp_length

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_mp_length` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PyMapping_Size()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Size) and [`PyObject_Size()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Size) make use of this function, and it shares their signature. You may set this slot to `NULL` when the object lacks a defined length.

 binaryfunc PyMappingMethods.mp_subscript

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_mp_subscript` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) and [`PySequence_GetSlice()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetSlice) make use of this function, and its signature matches that of `PyObject_GetItem()`. For the [`PyMapping_Check()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Check) function to yield `1` this slot has to be populated; otherwise it may be `NULL`.

 objobjargproc PyMappingMethods.mp_ass_subscript

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_mp_ass_subscript` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem), [`PyObject_DelItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelItem), [`PySequence_SetSlice()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_SetSlice) and [`PySequence_DelSlice()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_DelSlice) make use of this function. Its signature is the same as `PyObject_SetItem()`, except *v* may additionally be given as `NULL` so as to remove an item. When this slot holds `NULL`, the object provides no item assignment or deletion.

[Subject index](INDEX.md) · [Previous source contract](inplace-numeric-operation-slots.md) · [Following source contract](pysequencemethods-to-pysequencemethods-sq-inplace-concat.md)
