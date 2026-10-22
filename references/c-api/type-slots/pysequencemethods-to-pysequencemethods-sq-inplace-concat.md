# Sequence Object Structures

### Sequence Object Structures

 type PySequenceMethods

Pointers to the functions an object relies on to carry out the sequence protocol are stored in this structure.

 lenfunc PySequenceMethods.sq_length

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_length` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_Size()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Size) and [`PyObject_Size()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Size) make use of this function, and it shares their signature. It additionally serves to resolve negative indices through the `sq_item` and the `sq_ass_item` slots.

 binaryfunc PySequenceMethods.sq_concat

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_concat` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_Concat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Concat) makes use of this function and it shares the same signature. The `+` operator also relies on it, once numeric addition through the `nb_add` slot has been attempted.

 ssizeargfunc PySequenceMethods.sq_repeat

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_repeat` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_Repeat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Repeat) makes use of this function and it shares the same signature. The `*` operator also relies on it, once numeric multiplication through the `nb_multiply` slot has been attempted.

 ssizeargfunc PySequenceMethods.sq_item

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_item` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem) makes use of this function and it shares the same signature. [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) also relies on it, once subscription through the `mp_subscript` slot has been attempted. For the [`PySequence_Check()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Check) function to yield `1` this slot has to be populated; otherwise it may be `NULL`.

Negative indexes get treated this way: when the `sq_length` slot is populated, it is invoked and the sequence length serves to derive a positive index that gets handed to `sq_item`. When `sq_length` is `NULL`, the index reaches the function unchanged.

 ssizeobjargproc PySequenceMethods.sq_ass_item

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_ass_item` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_SetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_SetItem) makes use of this function and it shares the same signature. [`PyObject_SetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetItem) and [`PyObject_DelItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelItem) also rely on it, once item assignment and deletion through the `mp_ass_subscript` slot has been attempted. You may leave this slot as `NULL` when the object provides no item assignment or deletion.

 objobjproc PySequenceMethods.sq_contains

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_contains` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_Contains()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Contains) may make use of this function and it shares the same signature. You may leave this slot as `NULL`, in which case `PySequence_Contains()` merely walks the sequence until a match turns up.

 binaryfunc PySequenceMethods.sq_inplace_concat

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_inplace_concat` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[`PySequence_InPlaceConcat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_InPlaceConcat) makes use of this function and it shares the same signature. It ought to alter its first operand and give it back. You may leave this slot as `NULL`, in which case `PySequence_InPlaceConcat()` reverts to [`PySequence_Concat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Concat). The augmented assignment `+=` also relies on it, once numeric in-place addition through the `nb_inplace_add` slot has been attempted.

[Subject index](INDEX.md) · [Previous source contract](pymappingmethods-to-pymappingmethods-mp-ass-subscript.md) · [Following source contract](pysequencemethods-sq-inplace-repeat.md)
