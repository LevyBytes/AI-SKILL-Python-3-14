# type slots C API: Destructor garbage-collection and resurrection obligations

When the type participates in garbage collection (that is, the `Py_TPFLAGS_HAVE_GC` flag is enabled), the destructor must invoke [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack) prior to wiping out any member fields.

Invoking `tp_clear` from within `tp_dealloc` is allowed; doing so cuts down on duplicated code and ensures the object is consistently cleared ahead of destruction. Keep in mind, though, that `tp_clear` may already have run.

For a heap-allocated type (`Py_TPFLAGS_HEAPTYPE`), the deallocator must give up the owned reference it holds to its type object (through [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF)) once the type deallocator has finished. The example below demonstrates this.:

```c
static void
foo_dealloc(PyObject *op)
{
   foo_object *self = (foo_object *) op;
   PyObject_GC_UnTrack(self);
   Py_CLEAR(self->ref);
   Py_TYPE(self)->tp_free(self);
}

```

The exception status must remain untouched by `tp_dealloc`. Should it need to invoke anything capable of raising an exception, save the current exception state beforehand and put it back afterward (once any exceptions have been recorded with [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable)).

Example:

```c
static void
foo_dealloc(PyObject *self)
{
    PyObject *exc = PyErr_GetRaisedException();

    if (PyObject_CallFinalizerFromDealloc(self) < 0) {
        // self was resurrected.
        goto done;
    }

    PyTypeObject *tp = Py_TYPE(self);

    if (tp->tp_flags & Py_TPFLAGS_HAVE_GC) {
        PyObject_GC_UnTrack(self);
    }

    // Optional, but convenient to avoid code duplication.
    if (tp->tp_clear && tp->tp_clear(self) < 0) {
        PyErr_WriteUnraisable(self);
    }

    // Any additional destruction goes here.

    tp->tp_free(self);
    self = NULL;  // In case PyErr_WriteUnraisable() is called below.

    if (tp->tp_flags & Py_TPFLAGS_HEAPTYPE) {
        Py_CLEAR(tp);
    }

done:
    // Optional, if something was called that might have raised an
    // exception.
    if (PyErr_Occurred()) {
        PyErr_WriteUnraisable(self);
    }
    PyErr_SetRaisedException(exc);
}

```

Any Python thread may invoke `tp_dealloc`, not only the one that originally created the object (should the object end up inside a refcount cycle, that cycle may be reclaimed during a garbage collection running on any thread). For Python API calls this poses no difficulty, because the thread running `tp_dealloc` does so with an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). That said, when the object under destruction proceeds to tear down objects belonging to some external C library, you should make certain that releasing those objects on the thread that called `tp_dealloc` does not break any of the library's expectations.

**Inheritance:**

This field is inherited by subtypes.

See also

[Object Life Cycle](https://docs.python.org/3.14/c-api/lifecycle.html#life-cycle) for details about how this slot relates to other slots.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [API declaration, ownership, ABI and error contract](pytypeobject-tp-dealloc.md) · [Following source contract](pytypeobject-tp-vectorcall-offset-to-pytypeobject-tp-repr.md)
