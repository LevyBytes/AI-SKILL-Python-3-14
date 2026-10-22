# allocating objects on the heap C API: `_PyObject_New()`, `_PyObject_NewVar()`, `PyObject_Init()`, `PyObject_InitVar()`, `PyObject_New()`, `PyObject_Free()`, `PyObject_GC_New`, `PyType_GenericAlloc()`

## Allocating objects on the heap

### Allocating objects on the heap

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *_PyObject_New([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

*Return value: New reference.*

 [PyVarObject](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) *_PyObject_NewVar([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: New reference.*

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Init([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set up a freshly allocated object *op*, giving it its type plus a starting reference, and hand back that prepared object. The remaining fields stay untouched. The name is misleading: this has nothing to do with the object’s [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method (the [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) slot) — in particular, it will **not** invoke that `__init__()` method.

Treat this as a low-level helper overall. Wherever you can, reach for [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) instead. When you supply `tp_alloc` for a type of your own, favor [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) or `PyObject_New()`.

Note

Only the portion of memory matching the leading [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) structure gets set up by this call; everything beyond that is left as-is, not zeroed.

 [PyVarObject](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) *PyObject_InitVar([PyVarObject](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) *op, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Beyond carrying out all that `PyObject_Init()` performs, this additionally records the length data needed for a variable-size object.

Note

Just part of the object’s memory is prepared by this call; the remainder is not cleared to zero.

 PyObject_New(TYPE, typeobj)

Creates a fresh Python object from the C structure type *TYPE* together with the Python type object *typeobj* (`PyTypeObject*`): it reserves storage via [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc) and then sets it up the way `PyObject_Init()` would. Whoever calls it holds the sole reference (so the reference count starts at one).

Don’t reach for this directly when allocating an object’s memory; go through the type’s [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot.

While filling in a type’s [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot, lean on [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) rather than a hand-rolled function whose only job is to wrap this macro.

None of [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc), [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) ([`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__)), or [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) ([`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__)) is invoked by this macro.

Objects carrying [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) in their [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) cannot use this; reach for [`PyObject_GC_New`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) in that case.

Whatever this macro allocates has to be released through [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) (typically reached via the object’s [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot).

Note

There’s no promise that the block of memory handed back was wholly zeroed prior to being initialized.

Note

Rather than building a fully set-up object of that type, this macro simply grabs memory and readies it so [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) can finish the job later. When you want a fully initialized object, call *typeobj* directly. As an illustration:

```c
PyObject *foo = PyObject_CallNoArgs((PyObject *)&PyFoo_Type);

```

See also

- [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free)

- [`PyObject_GC_New`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New)

- [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc)

- [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc)

[Subject index](INDEX.md) · [Previous source contract](../abstract-objects-layer/abstract-objects-layer.md) · [Following source contract](pyobject-newvar-to-py-nonestruct.md)
