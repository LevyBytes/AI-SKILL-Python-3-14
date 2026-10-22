# destructor PyTypeObject.tp_finalize

destructor [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_finalize

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_finalize` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

A nullable pointer to an instance finalization function. It is the C implementation of the [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) special method. Its signature is:

```c
void tp_finalize(PyObject *self);

```

Finalization exists chiefly to carry out any substantial cleanup that has to happen before the object is destroyed, while the object together with everything it references directly or indirectly remains in a consistent state. Arbitrary Python code may run inside the finalizer.

By the time Python automatically finalizes an object, a number of that object’s direct or indirect referents may already have been automatically finalized themselves. None of the referents, however, will yet have been automatically cleared (`tp_clear`).

Because still-unfinalized objects may continue to use a finalized object, the finalizer has to leave the object in a sane state (for instance, with its invariants intact).

Note

Once Python has automatically finalized an object, it may begin automatically clearing (`tp_clear`) that object along with its direct and indirect referents. Cleared objects offer no guarantee of being in a consistent state; a finalized object must cope with referents that have been cleared.

Note

There is no guarantee that an object will be automatically finalized ahead of the call to its destructor (`tp_dealloc`). The recommendation is to call [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc) at the start of `tp_dealloc` so the object is always finalized before being destroyed.

Note

Any thread may call the `tp_finalize` function, though the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) will be held.

Note

The `tp_finalize` function may run during shutdown, once some global variables have already been deleted. Consult the documentation of the [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method for the particulars.

Python finalizes an object as though by the following algorithm:

1.

Python may flag the object as *finalized*. At present, Python always flags objects whose type supports garbage collection (that is, `tp_flags` has the `Py_TPFLAGS_HAVE_GC` flag set) and never flags other kinds of objects; this could change in a later version.

2.

When the object is not flagged as *finalized* and its `tp_finalize` finalizer function is non-`NULL`, that finalizer function runs.

3.

When the finalizer function ran and that finalizer rendered the object reachable (that is, a reference to the object exists and it is no longer a member of a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate)), the finalizer is said to have *resurrected* the object. Whether the finalizer can also resurrect the object by adding a fresh reference that does not render it reachable, leaving the object (still) a member of a cyclic isolate, is unspecified.

4.

When the finalizer resurrected the object, the object’s pending destruction is called off and its *finalized* flag may be cleared if it was set. At present, Python never clears the *finalized* flag; this could change in a later version.

*Automatic finalization* means any finalization Python performs other than through calls to [`PyObject_CallFinalizer()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizer) or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc). Nothing is promised about when, whether, or how frequently an object gets automatically finalized, apart from:

- Python will not automatically finalize an object while it is reachable, that is, while a reference to it exists and it is not a member of a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate).

- Python will not automatically finalize an object when doing so would not flag the object as *finalized*. At present this covers objects whose type does not support garbage collection, that is, those without the `Py_TPFLAGS_HAVE_GC` flag set. Such objects may still be finalized by hand through a call to [`PyObject_CallFinalizer()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizer) or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc).

- Python will not automatically finalize two members of the same [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) at the same time.

- Python will not automatically finalize an object once it has automatically cleared (`tp_clear`) that object.

-

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Continued contract in following source](pyobject-callfinalizer.md) · [Previous source contract](pytypeobject-tp-subclasses-to-pytypeobject-tp-version-tag.md)
