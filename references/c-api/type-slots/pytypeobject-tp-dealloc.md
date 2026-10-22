# type slots C API: Type destructor slot and lifecycle contract

destructor [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_dealloc

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_dealloc` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A pointer to the function that destroys an instance. Its signature reads:

```c
void tp_dealloc(PyObject *self);

```

What the destructor function should do is drop every reference the instance owns (for instance, via [`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR)), release all of the memory buffers the instance holds, and invoke the type's `tp_free` function to release the object itself.

Should you invoke functions capable of setting the error indicator, you have to rely on [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) and [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) so that an already-present error indicator isn't clobbered (the deallocation might well have happened in the middle of handling some other error):

```c
static void
foo_dealloc(foo_object *self)
{
    PyObject *et, *ev, *etb;
    PyObject *exc = PyErr_GetRaisedException();
    ...
    PyErr_SetRaisedException(exc);
}

```

The dealloc handler itself is not permitted to raise an exception; on reaching an error case it ought to invoke [`PyErr_FormatUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_FormatUnraisable) so as to log (and then clear) an unraisable exception.

When an object gets destroyed carries no guarantees, apart from these:

- Once the last reference to an object is gone, Python destroys it either right away or at some later point, save where its finalizer (`tp_finalize`) goes on to resurrect the object.

- While an object undergoes automatic finalization (`tp_finalize`) or automatic clearing (`tp_clear`), it will not be destroyed.

At present CPython destroys an object straight away from within [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) the moment the new reference count reaches zero, though a later release may alter this.

The advice is to invoke [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc) at the start of `tp_dealloc`, ensuring the object is invariably finalized ahead of being destroyed.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Continued contract in following source](destructor-pytypeobject-tp-dealloc.md)
