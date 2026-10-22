# object protocol C API: Truth tests, size, item access and iterator entrypoints

int PyObject_IsTrue([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields `1` when the object *o* counts as true, and `0` if it does not. The behavior matches the Python expression `not not o`. Should something go wrong, the result is `-1`.

 int PyObject_Not([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields `0` when the object *o* counts as true, and `1` if it does not. The behavior matches the Python expression `not o`. Should something go wrong, the result is `-1`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Type([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Provided *o* is non-`NULL`, this hands back a type object that matches the object type of *o*. Should it fail, it raises [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) and yields `NULL`. The behavior matches the Python expression `type(o)`. A new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the returned value is produced by this call. Apart from cases where a fresh strong reference is required, you have no real reason to call this rather than the [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) function, whose result is a pointer of type [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject)*.

 int PyObject_TypeCheck([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

Yield a non-zero result when the object *o* has type *type* or some subtype of *type*; otherwise yield `0`. Neither argument may be `NULL`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyObject_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyObject_Length([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the length of object *o*. Where *o* implements the sequence or mapping protocols, you get the sequence length back. A failure yields `-1`. This corresponds to the Python expression `len(o)`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyObject_LengthHint([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) defaultvalue)

Provide an approximate length for the object *o*. The call first attempts the true length, then falls back to an estimate via [`__length_hint__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__length_hint__), and lastly hands back the supplied default. A failure yields `-1`. This corresponds to the Python expression `operator.length_hint(o, defaultvalue)`.

Added in version 3.4.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the element of *o* that matches the object *key*, or `NULL` on a failure. This corresponds to the Python expression `o[key]`.

 int PyObject_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *v)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Associate the object *key* with the value *v*. A failure raises an exception and yields `-1`; success yields `0`. This corresponds to the Python statement `o[key] = v`. This call *does not* steal a reference to *v*.

 int PyObject_DelItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Delete the mapping for the object *key* out of the object *o*. A failure yields `-1`. This corresponds to the Python statement `del o[key]`.

 int PyObject_DelItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, const char *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves identically to `PyObject_DelItem()`, except that *key* is supplied as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Dir([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This corresponds to the Python expression `dir(o)`; it hands back a list of strings (possibly empty) suited to the object argument, or `NULL` should an error occur. Passing `NULL` as the argument mirrors the Python `dir()` and yields the names among the present locals; here, when no execution frame is running, `NULL` comes back yet [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) will report false.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GetIter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This corresponds to the Python expression `iter(o)`. It hands back a fresh iterator for the object argument, or the same object when that object is already an iterator. It raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and yields `NULL` whenever the object does not support iteration.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_SelfIter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This corresponds to the Python `__iter__(self): return self` method. Its purpose is to serve [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) types, plugging into the [`PyTypeObject.tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-hashnotimplemented.md) · [Following source contract](pyobject-getaiter-to-pyunstable-object-enabledeferredrefcount.md)
