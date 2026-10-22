# type objects C API: Type watchers, inheritance tests, allocation and names

int PyType_Unwatch(int watcher_id, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type)

Flag *type* as no longer watched, reversing an earlier `PyType_Watch()` call. *type* may not be `NULL`.

Extensions must never invoke this function using a *watcher_id* that was not handed to them by an earlier `PyType_AddWatcher()` call.

When it succeeds the function returns `0`. When it fails the function returns `-1` and leaves an exception set.

Added in version 3.12.

 typedef int (*PyType_WatchCallback)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type)

The type signature of a type-watcher callback function.

The callback may neither alter *type* nor trigger `PyType_Modified()` against *type* or any type within its MRO; breaking this rule risks infinite recursion.

Added in version 3.12.

 int PyType_HasFeature(PyTypeObject *o, int feature)

Returns a non-zero value when the type object *o* has the feature *feature* set. Each type feature is represented by an individual bit flag.

 int PyType_FastSubclass(PyTypeObject *type, int flag)

Returns a non-zero value when the type object *type* has the subclass flag *flag* set. The subclass flags carry the names [`Py_TPFLAGS_*_SUBCLASS`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_LONG_SUBCLASS). Numerous `_Check` functions for common types rely on this routine.

See also

[`PyObject_TypeCheck()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_TypeCheck), the slower fallback used inside `_Check` functions for types that lack subclass flags.

 int PyType_IS_GC(PyTypeObject *o)

Returns true when the type object carries support for the cycle detector; the check inspects the type flag [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC).

 int PyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Returns true when *a* is a subtype of *b*.

The check applies only to genuine subtypes, so [`__subclasscheck__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__subclasscheck__) is never invoked on *b*. To run the same test that [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) performs, call [`PyObject_IsSubclass()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_IsSubclass) instead.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GenericAlloc(PyTypeObject *type, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) nitems)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The generic implementation for a type object's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot. It draws on Python's standard memory allocation scheme to reserve space for a fresh instance, zeroes that space, and then sets it up as though [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) or [`PyObject_InitVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_InitVar) had run.

Don't invoke this routine directly to obtain memory for an object; go through the type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot instead.

When a type opts into garbage collection (that is, the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag is present), this routine acts like [`PyObject_GC_New`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) or [`PyObject_GC_NewVar`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar) (with the added guarantee that memory is zeroed prior to initialization), and you should match it with [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del) inside [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free). In the absence of that flag, it acts like [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New) or [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) (again with memory zeroed before initialization) and you should match it with [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) inside `tp_free`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GenericNew(PyTypeObject *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwds)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The generic implementation for a type object's [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) slot. It produces a fresh instance by way of the type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot and hands back the resulting object.

 int PyType_Ready(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Complete the setup of a type object. Run this on every type object to wrap up its initialization. The routine takes care of pulling in inherited slots from a type's base class. It returns `0` when it succeeds, or returns `-1` and sets an exception on failure.

Note

If one of the base classes implements the GC protocol while the type at hand omits [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) from its flags, the GC protocol gets inherited automatically from the parents. Conversely, when the type being built does carry `Py_TPFLAGS_HAVE_GC` among its flags, it **must** supply the GC protocol on its own, at minimum by providing the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handle.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetName(PyTypeObject *type)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Returns the type's name, the same as reading the type's [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) attribute.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetQualName(PyTypeObject *type)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Returns the type's qualified name, the same as reading the type's [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#type.__qualname__) attribute.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-to-pytype-watch.md) · [Following source contract](pytype-getfullyqualifiedname-to-pytype-getmodulebydef.md)
