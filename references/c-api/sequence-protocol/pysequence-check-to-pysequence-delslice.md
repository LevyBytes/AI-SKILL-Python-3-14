# sequence protocol C API: Sequence checks, item access and slice mutation

# Sequence

### Sequence Protocol

 int PySequence_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields `1` when the object implements the sequence protocol; otherwise the result is `0`. Keep in mind that a `1` also comes back for Python classes that define a [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method, with the exception of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) subclasses, because there is generally no way to tell which key types such a class will accept. This call can never fail.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySequence_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySequence_Length([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success, gives back how many objects the sequence *o* holds; a `-1` signals failure. It mirrors what the Python expression `len(o)` produces.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_Concat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success, hands back *o1* joined to *o2*; should it fail, the result is `NULL`. It corresponds to the Python expression `o1 + o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_Repeat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) count)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back the outcome of repeating the sequence object *o* a total of *count* times, or `NULL` if the call fails. It matches the Python expression `o * count`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_InPlaceConcat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o1, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

On success, hands back *o1* joined to *o2*; a failure yields `NULL`. Whenever *o1* allows it, the work happens *in-place*. It corresponds to the Python expression `o1 += o2`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_InPlaceRepeat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) count)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back the outcome of repeating the sequence object *o* a total of *count* times, or `NULL` if it fails. The work is carried out *in-place* whenever *o* allows it. It matches the Python expression `o *= count`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives back item number *i* from *o*, or `NULL` should the call fail. It corresponds to the Python expression `o[i]`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySequence_GetSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i1, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i2)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives back the portion of the sequence object *o* spanning *i1* through *i2*, or `NULL` if it fails. It corresponds to the Python expression `o[i1:i2]`.

 int PySequence_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Store the object *v* at position *i* within *o*. On failure, an exception is raised and `-1` comes back; success yields `0`. It corresponds to the Python statement `o[i] = v`. Note that this routine *does not* steal a reference to *v*.

Passing `NULL` for *v* removes the element, though relying on that behaviour is deprecated; prefer `PySequence_DelItem()` instead.

 int PySequence_DelItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Remove item number *i* from object *o*. A `-1` comes back when it fails. It corresponds to the Python statement `del o[i]`.

 int PySequence_SetSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i1, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i2, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Put the sequence object *v* into the portion of sequence object *o* running from *i1* up to *i2*. It corresponds to the Python statement `o[i1:i2] = v`.

 int PySequence_DelSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i1, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i2)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Drop the portion of sequence object *o* that runs from *i1* up to *i2*. A `-1` comes back on failure. It corresponds to the Python statement `del o[i1:i2]`.

[Subject index](INDEX.md) · [Following source contract](pysequence-count-to-pysequence-item.md)
