# Slice Objects

## Slice Objects

### Slice Objects

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PySlice_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object that backs slice objects. It matches [`slice`](https://docs.python.org/3.14/library/functions.html#slice) at the Python layer.

 int PySlice_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yield true when *ob* is a slice object; *ob* may not be `NULL`. This function always succeeds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySlice_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *start, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *stop, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *step)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield a fresh slice object built from the supplied values. The *start*, *stop*, and *step* parameters become the values of the slice object attributes carrying those same names. Any of the values may be `NULL`; when one is, `None` fills in for that attribute.

Yield `NULL` with an exception set when the new object could not be allocated.

 int PySlice_GetIndices([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *slice, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *stop, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *step)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Pull the start, stop and step indices out of the slice object *slice*, presuming a sequence whose length is *length*. Indices exceeding *length* are treated as errors.

On success this returns `0`; otherwise it returns `-1` on error, leaving no exception set, except where an index that was not `None` could not be coerced into an integer, in which case the returned `-1` does carry an exception set.

You most likely have no reason to call this function.

Changed in version 3.2: Previously the type for the *slice* parameter had been `PySliceObject*`.

 int PySlice_GetIndicesEx([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *slice, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *stop, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *step, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *slicelength)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A workable stand-in for `PySlice_GetIndices()`. Pull the start, stop, and step indices out of the slice object *slice* presuming a sequence whose length is *length*, and place the slice's length into *slicelength*. Indices that fall out of bounds get clipped in a way that lines up with how ordinary slices are handled.

Yield `0` on success and `-1` on error with an exception set.

Note

This function is regarded as unsafe for resizable sequences. Calls to it should be swapped for a pairing of `PySlice_Unpack()` and `PySlice_AdjustIndices()`, where

```c
if (PySlice_GetIndicesEx(slice, length, &start, &stop, &step, &slicelength) < 0) {
    // return error
}

```

becomes

```c
if (PySlice_Unpack(slice, &start, &stop, &step) < 0) {
    // return error
}
slicelength = PySlice_AdjustIndices(length, &start, &stop, step);

```

Changed in version 3.2: Previously the type for the *slice* parameter had been `PySliceObject*`.

Changed in version 3.6.1: When `Py_LIMITED_API` is unset or set to a value in the range `0x03050400` through `0x03060000` (exclusive) or `0x03060100` or above, `PySlice_GetIndicesEx()` is built as a macro on top of `PySlice_Unpack()` and `PySlice_AdjustIndices()`. The *start*, *stop* and *step* arguments are evaluated more than once.

Deprecated since version 3.6.1: When `Py_LIMITED_API` is set to a value below `0x03050400` or in the range `0x03060000` through `0x03060100` (exclusive), `PySlice_GetIndicesEx()` is a deprecated function.

 int PySlice_Unpack([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *slice, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *stop, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *step)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Pull the start, stop and step data members out of a slice object as C integers. Quietly clamp values above `PY_SSIZE_T_MAX` down to `PY_SSIZE_T_MAX`, quietly lift the start and stop values that fall below `PY_SSIZE_T_MIN` up to `PY_SSIZE_T_MIN`, and quietly lift the step values that fall below `-PY_SSIZE_T_MAX` up to `-PY_SSIZE_T_MAX`.

Yield `-1` with an exception set on error, `0` on success.

Added in version 3.6.1.

[Subject index](INDEX.md) · [Previous source contract](../set-objects/pyset-minsize.md) · [Following source contract](pyslice-adjustindices.md)
