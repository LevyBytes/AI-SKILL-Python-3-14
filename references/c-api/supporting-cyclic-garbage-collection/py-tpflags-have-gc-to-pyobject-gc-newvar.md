# supporting cyclic garbage collection C API: `Py_TPFLAGS_HAVE_GC`, `PyObject_GC_New()`, `PyObject_GC_Del()`, `PyObject_New`, `PyType_GenericAlloc()`, `PyObject_GC_NewVar()`

## Supporting Cyclic Garbage Collection

### Supporting Cyclic Garbage Collection

For Python to find and reclaim garbage tangled up in circular references, the object types acting as “containers” of other objects (which may themselves be containers) have to cooperate. A type that keeps no references to other objects, or that only references atomic types like numbers or strings, owes no explicit cooperation with garbage collection.

Making a container type means the type object's [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) field has to carry the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) and supply a [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler. Where the type's instances are mutable, you must additionally furnish a [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) implementation.

[`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC)

Any object whose type carries this flag has to abide by the rules set out here. As shorthand, such objects are called container objects.

Constructors of container types must observe two rules:

1.

Allocate the object's memory through `PyObject_GC_New` or `PyObject_GC_NewVar`.

2.

After every field that could hold references to other containers has been initialized, the constructor has to call `PyObject_GC_Track()`.

In the same vein, the object's deallocator has to follow a matching pair of rules:

1.

Ahead of invalidating any fields that point at other containers, `PyObject_GC_UnTrack()` has to be called.

2.

Free the object's memory by way of `PyObject_GC_Del()`.

Warning

Once a type takes on the Py_TPFLAGS_HAVE_GC, it *must* supply at least a [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler, or else deliberately borrow one from a subclass of its own.

If you call [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready), or one of the APIs that reach it indirectly such as [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) or [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), the interpreter fills in the [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags), [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) and [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) fields on its own — provided the type derives from a class that already implements the garbage collector protocol and the child class itself does *not* carry the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag.

 PyObject_GC_New(TYPE, typeobj)

The counterpart of [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New), but aimed at container objects that have the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag set.

Never invoke this straight to allocate an object's memory; go through the type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot instead.

While filling a type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot, lean on [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) rather than rolling a custom function that just wraps this macro.

Whatever memory this macro hands out has to be released with `PyObject_GC_Del()` (typically reached through the object's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot).

See also

- `PyObject_GC_Del()`

- [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New)

- [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc)

- [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc)

 PyObject_GC_NewVar(TYPE, typeobj, size)

The counterpart of [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar), but aimed at container objects that have the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag set.

Never invoke this straight to allocate an object's memory; route it through the type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot instead.

When you populate a type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot, favor [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) over a bespoke function that merely wraps this macro.

Whatever memory this macro provides must be released with `PyObject_GC_Del()` (usually via the object's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot).

See also

- `PyObject_GC_Del()`

-

[Subject index](INDEX.md) · [Previous source contract](../orientation/overview.md) · [Following source contract](pyobject-newvar-to-pyobject-gc-del.md)
