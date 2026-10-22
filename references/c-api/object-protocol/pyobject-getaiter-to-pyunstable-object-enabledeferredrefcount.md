# object protocol C API: `PyObject_GetAIter()`, `PyObject_GetTypeData()`, `PyType_GetTypeDataSize()`, `PyObject_GetItemData()`, `PyObject_VisitManagedDict()`, `PyObject_ClearManagedDict()`, `PyUnstable_Object_EnableDeferredRefcount()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_GetAIter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

This corresponds to the Python expression `aiter(o)`. It accepts an `AsyncIterable` object and produces an `AsyncIterator` from it. Usually that is a fresh iterator, though when the argument is already an `AsyncIterator` the call returns itself. It raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and yields `NULL` whenever the object does not support iteration.

Added in version 3.10.

 void *PyObject_GetTypeData([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *cls)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Obtain a pointer to the subclass-specific data set aside for *cls*.

The object *o* has to be an instance of *cls*, and *cls* has to have been built with a negative [`PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize). Python performs no such verification.

When an error occurs, set an exception and yield `NULL`.

Added in version 3.12.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyType_GetTypeDataSize([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *cls)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Hand back the size of the instance memory region set aside for *cls* ? that is, the size of the memory that `PyObject_GetTypeData()` returns.

This figure can exceed what was requested through [`-PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize); relying on the larger size is safe (for instance with `memset()`).

The type *cls* **must** have been built with a negative [`PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize). Python performs no such verification.

When an error occurs, set an exception and yield a negative value.

Added in version 3.12.

 void *PyObject_GetItemData([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Obtain a pointer to the per-item data for a class carrying [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END).

When an error occurs, set an exception and yield `NULL`. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when *o* lacks the [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END) flag.

Added in version 3.12.

 int PyObject_VisitManagedDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [visitproc](https://docs.python.org/3.14/c-api/gcsupport.html#c.visitproc) visit, void *arg)

Visit the managed dictionary belonging to *obj*.

You may invoke this function only within a traverse function of a type that carries the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) flag.

Added in version 3.13.

 void PyObject_ClearManagedDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Clear the managed dictionary belonging to *obj*.

You may invoke this function only within a clear function of a type that carries the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) flag.

Added in version 3.13.

 int PyUnstable_Object_EnableDeferredRefcount([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Turn on [deferred reference counting](https://peps.python.org/pep-0703/#deferred-reference-counting) for *obj*, where the runtime supports it. Within the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, this lets the interpreter skip reference count adjustments to *obj*, potentially improving multi-threaded performance. In exchange, *obj* gets deallocated solely by the tracing garbage collector, rather than at the moment the interpreter holds no further references to it.

The call hands back `1` when deferred reference counting becomes enabled on *obj*, and `0` when deferred reference counting is unsupported or the hint was disregarded by the interpreter ? for example where *obj* already has deferred reference counting enabled. The function is thread-safe and cannot fail.

On builds where the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) is enabled, which lack support for deferred reference counting, the call has no effect. Likewise it has no effect when *obj* is not an object tracked by the garbage collector (consult [`gc.is_tracked()`](https://docs.python.org/3.14/library/gc.html#gc.is_tracked) and [`PyObject_GC_IsTracked()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_IsTracked)).

The intended use is shortly after *obj* comes into being, from within the code that builds it ? such as inside the object's [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) slot.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-istrue-to-pyobject-selfiter.md) · [Following source contract](object-unique-reference-and-immortality-checks.md)
