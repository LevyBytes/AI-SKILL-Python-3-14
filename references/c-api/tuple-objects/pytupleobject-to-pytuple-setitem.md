# tuple objects C API: Tuple construction, size, item access and assignment

## Tuple Objects

### Tuple Objects

 type PyTupleObject

A Python tuple object is represented by this subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyTuple_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance stands for the Python tuple type; at the Python level it is the very same object as [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

 int PyTuple_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Yield true when *p* is a tuple object or an instance of some subtype of the tuple type. Success is guaranteed for this function.

 int PyTuple_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Yield true when *p* is a tuple object yet not an instance of any subtype of the tuple type. Success is guaranteed for this function.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTuple_New([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a freshly created tuple object whose size is *len*, or `NULL` together with a set exception on failure.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTuple_Pack([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) n, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a freshly created tuple object of size *n*, or `NULL` together with a set exception on failure. The tuple's entries are filled from the following *n* C arguments, each pointing to a Python object. `PyTuple_Pack(2, a, b)` matches `Py_BuildValue("(OO)", a, b)`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyTuple_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Given a pointer to a tuple object, hand back that tuple's size. When an error occurs, return `-1` along with a set exception.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyTuple_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Like `PyTuple_Size()`, but without error checking.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTuple_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the object sitting at index *pos* inside the tuple that *p* points to. When *pos* is negative or out of range, return `NULL` and raise an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception.

The reference you get back is borrowed from the tuple *p* (meaning: it remains valid only while you keep a reference to *p*). For a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), reach for [`Py_NewRef(PyTuple_GetItem(...))`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef) or [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTuple_GET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos)

*Return value: Borrowed reference.*

Like `PyTuple_GetItem()`, but does no checking of its arguments.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTuple_GetSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) low, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) high)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the slice spanning *low* through *high* of the tuple that *p* points to, or `NULL` plus a set exception on failure.

This mirrors the Python expression `p[low:high]`. There is no support for indexing relative to the tuple's end.

 int PyTuple_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Place a reference to object *o* at index *pos* within the tuple that *p* points to. Return `0` when this succeeds. Should *pos* fall out of range, return `-1` and raise an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception.

Note

This function “steals” a reference to *o* while releasing whatever reference the tuple previously held at that position.

[Subject index](INDEX.md) · [Previous source contract](../thread-local-storage-support/pythread-create-key-to-pythread-reinittls.md) · [Following source contract](pytuple-set-item-to-pytuple-resize.md)
