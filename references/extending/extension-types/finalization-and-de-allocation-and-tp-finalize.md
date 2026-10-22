# Finalization and De-allocation — tp_dealloc, PyObject, Py_TYPE, tp_free, PyObject_GC_UnTrack, Py_CLEAR, PyErr_Fetch, PyErr_Restore, PyObject_CallNoArgs, PyErr_WriteUnraisable, Py_DECREF, tp_traverse, PyTypeObject, tp_clear, tp_finalize

### 3.1. Finalization and De-allocation

```c
destructor tp_dealloc;

```

The interpreter invokes this function once your type's instance has its reference count drop to zero and Python is ready to reclaim that instance. Should your type hold memory that needs releasing, or any other tidy-up to carry out, this is the place for it. The object itself must also be released right here. The function might look like this:

```c
static void
newdatatype_dealloc(PyObject *op)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    free(self->obj_UnderlyingDatatypePtr);
    Py_TYPE(self)->tp_free(self);
}

```

When garbage collection is supported by your type, the destructor needs to invoke [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack) prior to wiping out any member fields:

```c
static void
newdatatype_dealloc(PyObject *op)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    PyObject_GC_UnTrack(op);
    Py_CLEAR(self->other_obj);
    ...
    Py_TYPE(self)->tp_free(self);
}

```

A critical rule for the deallocator function is that it must leave any outstanding exceptions untouched. The reason this matters: deallocators routinely fire while the interpreter is unwinding Python's stack, and when that unwinding stems from an exception (instead of ordinary returns), there's no mechanism keeping deallocators from observing that an exception is already in place. Should a deallocator take any step that triggers further Python code to run, that step may notice an exception has been set. The result can be confusing errors emitted by the interpreter. To guard against this correctly, stash the outstanding exception before you carry out the risky step, then put it back afterward. The [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch) and [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore) functions let you do exactly that:

```c
static void
my_dealloc(PyObject *obj)
{
    MyObject *self = (MyObject *) obj;
    PyObject *cbresult;

    if (self->my_callback != NULL) {
        PyObject *err_type, *err_value, *err_traceback;

        /* This saves the current exception state */
        PyErr_Fetch(&err_type, &err_value, &err_traceback);

        cbresult = PyObject_CallNoArgs(self->my_callback);
        if (cbresult == NULL) {
           PyErr_WriteUnraisable(self->my_callback);
        }
        else {
            Py_DECREF(cbresult);
        }

        /* This restores the saved exception state */
        PyErr_Restore(err_type, err_value, err_traceback);

        Py_DECREF(self->my_callback);
    }
    Py_TYPE(self)->tp_free(self);
}

```

Note

What you can do safely inside a deallocator function has its limits. To begin with, when your type supports garbage collection (by way of [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) and/or [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear)), it's possible that some of the object's members were already cleared or finalized by the moment [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) runs. On top of that, while inside `tp_dealloc`, your object sits in a precarious condition: its reference count has hit zero. Any invocation of a non-trivial object or API (such as the one shown above) may circle back to `tp_dealloc` once more, producing a double free and a crash.

From Python 3.4 onward, the guidance is to avoid placing any intricate finalization logic inside [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc), and to rely instead on the newer [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) type method.

See also

[**PEP 442**](https://peps.python.org/pep-0442/) explains the new finalization scheme.

[Subject index](INDEX.md) · [Previous source section](type-name-size-and-documentation-fields.md) · [Next source section](object-repr-and-string-presentation.md)
