# tuple objects C API: `PyTuple_SET_ITEM()`, `_PyTuple_Resize()`

void PyTuple_SET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) pos, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Behaves like `PyTuple_SetItem()`, yet performs no error checking; reserve it *only* for populating freshly made tuples.

When Python is compiled in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions), the bounds check runs as an assertion.

Note

This function “steals” a reference to *o* and, in contrast to `PyTuple_SetItem()`, leaves untouched any reference to the item being replaced; whatever the tuple held at position *pos* gets leaked.

Warning

Reserve this macro strictly for tuples that have just been created. Applying it to a tuple already in circulation (put differently, one whose refcount > 1) may result in undefined behavior.

 int _PyTuple_Resize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **p, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) newsize)

Useful for resizing a tuple. The tuple's new length becomes *newsize*. Since tuples are *supposed* to stay immutable, reserve this for cases where exactly one reference to the object exists. Avoid it if the tuple might already be visible to some other portion of the code. Growth or shrinkage always happens at the tuple's tail. Picture it as discarding the old tuple and building a fresh one, merely with greater efficiency. Returns `0` on success. Calling code must never presume that the resulting `*p` matches what it was before this call. When the object that `*p` referenced is replaced, the original `*p` is destroyed. On failure, returns `-1`, sets `*p` to `NULL`, and raises [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) or [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytupleobject-to-pytuple-setitem.md) · [Following source contract](pystructsequence-newtype-to-pystructsequence-inittype2.md)
