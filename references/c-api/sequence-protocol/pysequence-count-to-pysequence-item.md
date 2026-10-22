# sequence protocol C API: Sequence search, conversion and fast item access

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySequence_Count([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Report how many times *value* shows up inside *o* — in other words, the count of keys where `o[key] == value`. Should it fail, `-1` is returned. It matches the Python expression `o.count(value)`.

 int PySequence_Contains([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Check whether *value* is present in *o*. When some entry of *o* equals *value*, the result is `1`; if not, it is `0`. Errors yield `-1`. It matches the Python expression `value in o`.

 int PySequence_In([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Alias for `PySequence_Contains()`.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.14: Fresh code ought to avoid calling this routine going forward.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySequence_Index([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the lowest index *i* satisfying `o[i] == value`. An error produces `-1`. It matches the Python expression `o.index(value)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_List([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a list object holding the same elements as the sequence or iterable *o*, or `NULL` if it fails. That list is always a freshly created one. It matches the Python expression `list(o)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_Tuple([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a tuple object holding the same elements as the sequence or iterable *o*, or `NULL` if it fails. When *o* is already a tuple, you get a new reference to it; otherwise a tuple is assembled from the matching contents. It matches the Python expression `tuple(o)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_Fast([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *m)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the sequence or iterable *o* in a form the rest of the `PySequence_Fast*` family of functions can work with. When the argument is neither a sequence nor an iterable, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised carrying *m* as its message text. A failure yields `NULL`.

The name `PySequence_Fast*` reflects how these routines treat *o* as either a [`PyTupleObject`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject) or a [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject), reaching straight into the data fields of *o*.

By way of a CPython implementation detail, an *o* that is already a sequence or list is handed straight back.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySequence_Fast_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Gives the length of *o*, on the premise that *o* came from `PySequence_Fast()` and is not `NULL`. You could also obtain the size by invoking `PySequence_Size()` on *o*, yet `PySequence_Fast_GET_SIZE()` runs quicker since it may take *o* to be a list or tuple.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_Fast_GET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i)

*Return value: Borrowed reference.*

Give back item number *i* of *o*, on the premise that *o* came from `PySequence_Fast()`, that *o* is not `NULL`, and that *i* stays within bounds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **PySequence_Fast_ITEMS([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Give back the raw array of PyObject pointers. Presumes *o* came from `PySequence_Fast()` and that *o* is not `NULL`.

Bear in mind that resizing a list can trigger a reallocation that moves the items array elsewhere. For that reason, rely on the raw array pointer solely where the sequence is guaranteed to stay fixed.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i)

*Return value: New reference.*

Give back item number *i* of *o*, or `NULL` if it fails. This is a quicker variant of `PySequence_GetItem()` that skips verifying that `PySequence_Check()` holds for *o* and does no remapping of negative indices.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pysequence-check-to-pysequence-delslice.md)
