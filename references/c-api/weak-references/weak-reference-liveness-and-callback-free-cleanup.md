# weak references C API: `PyWeakref_IsDead()`, `PyObject_ClearWeakRefs()`, `PyUnstable_Object_ClearWeakRefsNoCallbacks()`

int PyWeakref_IsDead([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ref)

Check whether the weak reference *ref* has died. It gives back 1 when the reference is dead, 0 when it remains alive, and -1 (with an error set) when *ref* isn't a weak reference object at all.

Added in version 3.14.

 void PyObject_ClearWeakRefs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) handler invokes this function in order to clear weak references.

It walks through every weak reference belonging to *object* and fires the callback on each reference that carries one. Once every callback has been tried, it returns.

 void PyUnstable_Object_ClearWeakRefsNoCallbacks([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object)

 *This counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It can change with no warning across minor releases.*

Wipes the weakrefs belonging to *object* while leaving the callbacks uncalled.

For types that carry finalizers (that is, [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__)), the [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) handler invokes this function. For such objects the handler runs `PyObject_ClearWeakRefs()` first to clear weakrefs and fire their callbacks, then the finalizer, and only at the end this function, to wipe any weakrefs the finalizer might have produced.

Under most conditions, clearing weakrefs through `PyObject_ClearWeakRefs()` is the better choice rather than this function.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyweakref-check-to-pyweakref-get-object.md)
