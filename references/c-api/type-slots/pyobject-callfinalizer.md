# type slots C API: `PyObject_CallFinalizer()`

When an object belongs to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), Python skips automatic finalization for it once any other member has been automatically cleared (refer to `tp_clear`).

- Each member of a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) gets automatically finalized by Python prior to any of them being automatically cleared (refer to `tp_clear`).

- Whenever Python intends to automatically clear an object (`tp_clear`), the object is automatically finalized beforehand.

At present, automatic finalization in Python applies solely to objects belonging to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), though later releases may finalize objects routinely ahead of destroying them.

For finalizing an object by hand, avoid invoking this function directly; instead invoke [`PyObject_CallFinalizer()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizer) or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc).

The exception state in effect should be preserved by `tp_finalize`. For a finalizer of any complexity, the suggested approach is to save the exception up front via [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) and to put it back at the close via [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException). Should an exception arise partway through the finalizer, record and discard it using [`PyErr_WriteUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WriteUnraisable) or [`PyErr_FormatUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_FormatUnraisable). As an illustration:

```c
static void
foo_finalize(PyObject *self)
{
    // Save the current exception, if any.
    PyObject *exc = PyErr_GetRaisedException();

    // ...

    if (do_something_that_might_raise() != success_indicator) {
        PyErr_WriteUnraisable(self);
        goto done;
    }

done:
    // Restore the saved exception.  This silently discards any exception
    // raised above, so be sure to call PyErr_WriteUnraisable first if
    // necessary.
    PyErr_SetRaisedException(exc);
}

```

**Inheritance:**

Subtypes inherit this field.

Added in version 3.4.

Changed in version 3.8: Prior to version 3.8, using this field required setting the `Py_TPFLAGS_HAVE_FINALIZE` flags bit. That step is no longer needed.

See also

- [**PEP 442**](https://peps.python.org/pep-0442/): “Safe object finalization”

- [Object Life Cycle](https://docs.python.org/3.14/c-api/lifecycle.html#life-cycle) for details about how this slot relates to other slots.

- [`PyObject_CallFinalizer()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizer)

-

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [API declaration, ownership, ABI and error contract](pytypeobject-tp-finalize.md) · [Following source contract](pyobject-callfinalizerfromdealloc-to-pytypeobject-tp-watched.md)
