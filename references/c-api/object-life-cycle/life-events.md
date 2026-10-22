# Life Events

### Life Events

The diagram that follows depicts the sequence of events possible across an object's lifetime. An arrow running from *A* to *B* signifies that event *B* may follow once event *A* has taken place, while the arrow's label states the condition required for *B* to follow *A*.

Explanation:

- When a new object is constructed by calling its type:

  1.

[`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) runs to bring a new object into being.

  2.

[`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) gets invoked straight from [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) in order to reserve the memory for the new object.

  3.

[`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) sets up the freshly built object. `tp_init` may be invoked once more to re-initialize an object should that be wanted. Alternatively, the `tp_init` call can be bypassed completely, as happens for instance when Python code invokes [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__).

- Once `tp_init` finishes, the object is fit for use.

- At some point following the removal of an object's final reference:

  1.

Should an object lack the *finalized* mark, it may be finalized: it gets marked as *finalized* and its [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) function is invoked. Python does *not* finalize an object the moment its last reference goes away; rely on `PyObject_CallFinalizerFromDealloc()` to guarantee `tp_finalize` always runs.

  2.

Once the object carries the finalized mark, the garbage collector may invoke [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) to release the references the object holds. This does *not* happen at the moment the object's reference count drops to zero.

  3.

[`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) runs to tear down the object. So as not to repeat code, `tp_dealloc` ordinarily delegates to [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) to release the object's references.

  4.

Upon [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) wrapping up the object's destruction, it invokes [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) directly (typically configured to [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) or [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del) automatically, whichever suits the type) to release the memory.

- The [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) function may, if it chooses, attach a reference to the object. Doing so *resurrects* the object and halts its imminent destruction. (Resurrecting an object is the exclusive privilege of `tp_finalize`; [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) and [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) cannot do so unless they call into `tp_finalize`.) Whether resurrecting an object strips its *finalized* mark is not guaranteed either way. As things stand, Python leaves the *finalized* mark in place on a resurrected object that supports garbage collection (that is, the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag is set) yet strips the mark when the object lacks garbage-collection support; one or both of these behaviors might be revised later on.

- [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) may, at its discretion, invoke [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) by way of `PyObject_CallFinalizerFromDealloc()` if it wants to repurpose that logic during object destruction. This is advised, as it ensures `tp_finalize` always runs ahead of destruction. Consult the `tp_dealloc` documentation for sample code.

- When the object belongs to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) and either [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) does not manage to sever the reference cycle or the cyclic isolate goes unnoticed (maybe [`gc.disable()`](https://docs.python.org/3.14/library/gc.html#gc.disable) was invoked, or the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag was mistakenly left off one of the types involved), the objects stay uncollectable forever (they "leak"). Refer to [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage).

When the object is flagged as supporting garbage collection (the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag is set within [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags)), these additional events can occur as well:

- From time to time the garbage collector invokes [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) to pick out [cyclic isolates](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate).

- Upon the garbage collector locating a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), it finalizes one member of the group by stamping it *finalized* and invoking its [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) function, should one be present. The process loops until either the cyclic isolate is gone or every object has been finalized.

- [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) may resurrect the object by introducing a reference originating outside the [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate). That fresh reference stops the cluster of objects from forming a cyclic isolate any longer (the reference cycle might persist, but where it does the objects are no longer isolated).

- Upon the garbage collector locating a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) whose member objects all bear the *finalized* mark already, the garbage collector clears one or more of the as-yet-uncleared objects in the group (possibly concurrently) by invoking each one's [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) function. This loops for as long as the cyclic isolate persists and not every object has been cleared.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](object-life-cycle.md) · [Following source contract](cyclic-isolate-destruction.md)
