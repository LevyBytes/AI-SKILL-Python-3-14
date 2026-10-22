# object protocol C API: `PyUnstable_TryIncRef()`, `PyUnstable_EnableTryIncRef()`

int PyUnstable_TryIncRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Bump the reference count of *obj* when that count is not zero. It hands back `1` when the object's reference count was incremented successfully. In any other case, the call returns `0`.

`PyUnstable_EnableTryIncRef()` has to have run beforehand on *obj*, or else this call may spuriously return `0` within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build).

Apart from behaving atomically within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), this call is logically the same as the C code below:

```c
if (Py_REFCNT(op) > 0) {
   Py_INCREF(op);
   return 1;
}
return 0;

```

The intent is to supply a building block for handling weak references without incurring the cost of a Python [weak reference object](https://docs.python.org/3.14/c-api/weakref.html#weakrefobjects).

In the usual case, using this function correctly calls for cooperation from *obj*'s deallocator ([`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc)). For instance, the sketch below could be tailored to build a "weakmap" behaving like a [`WeakValueDictionary`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakValueDictionary) for one particular type:

```c
PyMutex mutex;

PyObject *
add_entry(weakmap_key_type *key, PyObject *value)
{
    PyUnstable_EnableTryIncRef(value);
    weakmap_type weakmap = ...;
    PyMutex_Lock(&mutex);
    weakmap_add_entry(weakmap, key, value);
    PyMutex_Unlock(&mutex);
    Py_RETURN_NONE;
}

PyObject *
get_value(weakmap_key_type *key)
{
    weakmap_type weakmap = ...;
    PyMutex_Lock(&mutex);
    PyObject *result = weakmap_find(weakmap, key);
    if (PyUnstable_TryIncRef(result)) {
        // `result` is safe to use
        PyMutex_Unlock(&mutex);
        return result;
    }
    // if we get here, `result` is starting to be garbage-collected,
    // but has not been removed from the weakmap yet
    PyMutex_Unlock(&mutex);
    return NULL;
}

// tp_dealloc function for weakmap values
void
value_dealloc(PyObject *value)
{
    weakmap_type weakmap = ...;
    PyMutex_Lock(&mutex);
    weakmap_remove_value(weakmap, value);

    ...
    PyMutex_Unlock(&mutex);
}

```

Added in version 3.14.

 void PyUnstable_EnableTryIncRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Permit later calls to `PyUnstable_TryIncRef()` on *obj*. While calling this, the caller is required to hold a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to *obj*.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](object-unique-reference-and-immortality-checks.md) · [Following source contract](pyunstable-object-isuniquelyreferenced.md)
