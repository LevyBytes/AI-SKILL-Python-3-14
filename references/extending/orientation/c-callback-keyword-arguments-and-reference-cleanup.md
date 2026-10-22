# Calling Python callbacks with keyword arguments

Use an empty positional-argument tuple when passing only keyword arguments to
[`PyObject_Call`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call).
Its positional-argument object must not be NULL. Check both allocations before
calling Python; an allocation failure already sets the exception to propagate.

This helper calls `callback(name=value)`. The caller must hold a valid callable
reference and meet the C API's interpreter/thread-state requirements.

```c
#include <Python.h>

static PyObject *call_keyword_callback(PyObject *callback, int value)
{
    PyObject *args = PyTuple_New(0);
    if (args == NULL)
        return NULL;

    PyObject *kwargs = Py_BuildValue("{s:i}", "name", value);
    if (kwargs == NULL) {
        Py_DECREF(args);
        return NULL;
    }

    PyObject *result = PyObject_Call(callback, args, kwargs);
    Py_DECREF(args);
    Py_DECREF(kwargs);
    return result;
}
```

On success, the helper transfers the result's new reference to its caller, which
must eventually release it. On failure, it returns NULL with the Python exception
preserved. It releases its temporary tuple and dictionary in both call outcomes.

[Subject index](INDEX.md) · [Previous source section](calling-python-functions-from-c-and-pyerr-clear.md) · [Next source section](extension-argument-parsing-and-buffer-sizes.md) · [Owning section and setup](calling-python-functions-from-c-and-pyerr-clear.md) · [Preceding cross-file owner and contract](calling-python-functions-from-c.md)
