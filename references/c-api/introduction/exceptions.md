# Exceptions

### Exceptions

A Python programmer must concern themselves with exceptions only when particular error handling is wanted; exceptions left unhandled travel up automatically to the caller, then onward to that caller's caller, and so forth, until arriving at the top-level interpreter, where they're presented to the user along with a stack traceback.

In C, by contrast, error checking is always something you must do explicitly. Every function within the Python/C API may raise exceptions, save for those where a function's documentation states otherwise outright. As a rule, upon hitting an error a function sets an exception, releases whatever object references it holds, and hands back an error indicator. Absent documentation to the contrary, that indicator is either `NULL` or `-1`, contingent on the function's return type. Some functions yield a Boolean true/false outcome, where false signals an error. A small number of functions provide no clear error indicator or carry an ambiguous return value, demanding explicit error testing through [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred). Such cases are always spelled out in the documentation.

The exception state lives in per-thread storage (which amounts to using global storage in a program that isn't threaded). At any moment a thread sits in one of two conditions: either an exception has been raised, or it hasn't. To test this you can call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred): it yields a borrowed reference to the exception type object whenever an exception has occurred, and `NULL` otherwise. Several functions exist for setting the exception state: [`PyErr_SetString()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetString) is the function most commonly used (albeit not the most general) for establishing the exception state, while [`PyErr_Clear()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Clear) wipes it out.

The complete exception state comprises three objects (any of which may be `NULL`): the type of the exception, its matching exception value, and the traceback. They carry the same meanings as the Python result of `sys.exc_info()`; nevertheless, they aren't identical: the Python objects stand for the most recent exception handled by a Python [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) — [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statement, whereas the C-level exception state persists only while an exception travels among C functions before reaching the main loop of the Python bytecode interpreter, which is responsible for moving it over to `sys.exc_info()` and related items.

Be aware that, as of Python 1.5, the recommended, thread-safe approach for reaching the exception state from Python code is invoking the function [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info), which yields the per-thread exception state available to Python code. Additionally, the behavior of both routes to the exception state was altered such that any function catching an exception will store and later restore its thread's exception state, thereby keeping its caller's exception state intact. Doing so heads off frequent bugs in exception-handling code that arise when a harmless-seeming function clobbers the exception currently being processed; it likewise cuts down on the frequently undesired prolonged lifetime of objects kept alive by the stack frames in the traceback.

Speaking broadly, whenever a function calls some other function to carry out a task, it should verify whether the called function raised an exception and, if it did, relay the exception state onward to its own caller. It ought to release any object references it owns and return an error indicator, but it ought *not* raise a fresh exception — doing that would clobber the exception just raised and forfeit crucial detail about the precise source of the error.

A basic illustration of catching exceptions and forwarding them appears in the `sum_sequence()` example shown earlier. As it happens, that example has no owned references to tidy up when it spots an error. The example function that follows does demonstrate some error cleanup. To begin, as a reminder of what makes Python pleasant, here's the same thing written in Python:

```c
def incr_item(dict, key):
    try:
        item = dict[key]
    except KeyError:
        item = 0
    dict[key] = item + 1

```

And here's the matching C code, in its full splendor:

```c
int
incr_item(PyObject *dict, PyObject *key)
{
    /* Objects all initialized to NULL for Py_XDECREF */
    PyObject *item = NULL, *const_one = NULL, *incremented_item = NULL;
    int rv = -1; /* Return value initialized to -1 (failure) */

    item = PyObject_GetItem(dict, key);
    if (item == NULL) {
        /* Handle KeyError only: */
        if (!PyErr_ExceptionMatches(PyExc_KeyError))
            goto error;

        /* Clear the error and use zero: */
        PyErr_Clear();
        item = PyLong_FromLong(0L);
        if (item == NULL)
            goto error;
    }
    const_one = PyLong_FromLong(1L);
    if (const_one == NULL)
        goto error;

    incremented_item = PyNumber_Add(item, const_one);
    if (incremented_item == NULL)
        goto error;

    if (PyObject_SetItem(dict, key, incremented_item) < 0)
        goto error;
    rv = 0; /* Success */
    /* Continue with cleanup code */

 error:
    /* Cleanup code, shared by success and failure path */

    /* Use Py_XDECREF() to ignore NULL references */
    Py_XDECREF(item);
    Py_XDECREF(const_one);
    Py_XDECREF(incremented_item);

    return rv; /* -1 for error, 0 for success */
}

```

This sample stands as a sanctioned application of C's `goto` statement! It showcases how [`PyErr_ExceptionMatches()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_ExceptionMatches) and [`PyErr_Clear()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Clear) are used to deal with particular exceptions, plus how [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) is used to release owned references that might be `NULL` (observe the `'X'` within the name; [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) would crash if it met a `NULL` reference). For this to function it's essential that the variables holding owned references start out initialized to `NULL`; in the same way, the intended return value starts at `-1` (failure) and is switched to success only once the last call made succeeds.

[Subject index](INDEX.md) · [Previous source contract](py-ssize-t.md) · [Following source contract](embedding-python.md)
