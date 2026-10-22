# allocating objects on the heap C API: `PyObject_NewVar()`, `PyObject_Free()`, `PyObject_GC_NewVar`, `PyType_GenericAlloc()`

PyObject_NewVar(TYPE, typeobj, size)

Behaves as `PyObject_New` does, with these differences:

- Storage is reserved for the *TYPE* structure together with *size* (`Py_ssize_t`) trailing fields, each sized per the [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize) field of *typeobj*.

- That memory gets set up the way `PyObject_InitVar()` does.

This comes in handy for building objects such as tuples, whose size is fixed once they are constructed. Folding the field array into the very same allocation cuts the allocation count and makes memory handling more efficient.

Don’t reach for this directly when allocating an object’s memory; go through the type’s [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot.

While filling in a type’s [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot, lean on [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) rather than a hand-rolled function whose only job is to wrap this macro.

Objects carrying [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) in their [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) cannot use this; reach for [`PyObject_GC_NewVar`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar) in that case.

Whatever this function allocates has to be released through [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) (typically reached via the object’s [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot).

Note

Nothing guarantees that the memory you get back was fully cleared to zero ahead of its initialization.

Note

This macro stops short of producing a fully prepared object of the type; it only secures memory and gets it ready for [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) to complete the setup afterward. For a fully initialized object, invoke *typeobj* itself instead. For instance:

```c
PyObject *list_instance = PyObject_CallNoArgs((PyObject *)&PyList_Type);

```

See also

- [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free)

- [`PyObject_GC_NewVar`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar)

- [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc)

- [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) _Py_NoneStruct

The object that Python surfaces as `None`. Reach it solely through the [`Py_None`](https://docs.python.org/3.14/c-api/none.html#c.Py_None) macro, which resolves to a pointer aimed at this object.

See also

[Module Objects](https://docs.python.org/3.14/c-api/module.html#moduleobjects)

For allocating and building extension modules.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyobject-new-to-pytype-genericalloc.md) · [Following source contract](soft-deprecated-aliases.md)
