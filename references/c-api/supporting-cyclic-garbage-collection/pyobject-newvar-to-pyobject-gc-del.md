# supporting cyclic garbage collection C API: Garbage-collected allocation, tracking and deletion

[`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar)

- [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc)

- [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnstable_Object_GC_NewWithExtraData([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, size_t extra_size)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Much like `PyObject_GC_New`, except that it sets aside *extra_size* bytes past the object's end (at the [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) offset). That allocated region is zero-filled, apart from the [`Python object header`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

When the object goes away the extra data goes with it; beyond that, Python takes no charge of it.

Whatever memory this function returns has to be released with `PyObject_GC_Del()` (typically reached through the object's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot).

Warning

This function wears the unstable label because how extra data after an instance will ultimately be reserved has not been settled. When you need a variable count of fields, reach instead for [`PyVarObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) together with [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize).

Added in version 3.12.

 PyObject_GC_Resize(TYPE, op, newsize)

Resize an object that [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) allocated. Yields the resized object as type `TYPE*` (standing for any C type), or `NULL` if it fails.

Here *op* has to be of type [PyVarObject](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject)* and must not yet be under the collector's tracking, while *newsize* has to be of type [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t).

 void PyObject_GC_Track([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Brings the object *op* into the collector's set of tracked container objects. Because the collector may fire at unforeseen moments, an object has to stay valid the whole time it is tracked. Call this once every field reached by the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler has become valid — usually toward the constructor's end.

 int PyObject_IS_GC([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Gives back a non-zero value when the object implements the garbage collector protocol, and 0 otherwise.

When this function gives 0, the garbage collector is unable to track the object.

 int PyObject_GC_IsTracked([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Yields 1 when *op*'s object type implements the GC protocol and *op* is at present being tracked by the garbage collector; otherwise 0.

It parallels the Python function [`gc.is_tracked()`](https://docs.python.org/3.14/library/gc.html#gc.is_tracked).

Added in version 3.9.

 int PyObject_GC_IsFinalized([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Yields 1 when *op*'s object type implements the GC protocol and *op* has already been finalized by the garbage collector; otherwise 0.

It parallels the Python function [`gc.is_finalized()`](https://docs.python.org/3.14/library/gc.html#gc.is_finalized).

Added in version 3.9.

 void PyObject_GC_Del(void *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Frees memory that was handed to an object via `PyObject_GC_New` or `PyObject_GC_NewVar`.

Never invoke this straight to free an object's memory; go through the type's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot instead.

Do not apply it to memory that came from [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New), [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar), or kindred allocation functions; reach for [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) in those cases.

See also

- [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) plays the same role as this function for the non-GC case.

-

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-tpflags-have-gc-to-pyobject-gc-newvar.md) · [Following source contract](pyobject-gc-new-to-py-visit.md)
