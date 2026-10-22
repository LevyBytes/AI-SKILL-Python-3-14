# Intermezzo: Errors and Exceptions — PyErr_SetString, PyExc_ZeroDivisionError, PyErr_SetFromErrno, PyErr_SetObject, Py_INCREF, PyErr_Occurred, PyErr_, PyErr_Clear, PyErr_NoMemory, PyLong_FromLong, PyArg_ParseTuple, Py_XDECREF, Py_DECREF, PyExc_TypeError, PyExc_OSError, PyExc_ValueError, PyObject, PyErr_NewException, Py_mod_exec, PyExc_ImportError, PyModule_AddObjectRef, PyModuleDef_Slot, PyModuleDef, PyModuleDef_HEAD_INIT, PyMODINIT_FUNC, PyInit_spam, PyModuleDef_Init

### 1.2. Intermezzo: Errors and Exceptions

One important convention pervades the Python interpreter: a failing function should set an exception condition and hand back an error value (typically `-1` or a `NULL` pointer). Three members of the interpreter’s thread state hold the exception information. When no exception is active these are `NULL`. Otherwise they are the C counterparts of the members from the Python tuple that [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns. Those three are the exception type, the exception instance, and a traceback object. Grasping them matters for understanding how errors travel.

A variety of functions in the Python API exist to set various exception kinds.

By far the most frequent is [`PyErr_SetString()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetString). It accepts an exception object plus a C string. Typically the exception object is a predefined one such as [`PyExc_ZeroDivisionError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_ZeroDivisionError). The C string spells out what went wrong, gets converted into a Python string object, and is kept as the exception’s “associated value”.

Another handy one is [`PyErr_SetFromErrno()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetFromErrno); it accepts only an exception argument and builds the associated value by reading the global variable `errno`. The broadest of them is [`PyErr_SetObject()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetObject), accepting two object arguments — the exception together with its associated value. There is no need to [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) the objects you hand to any of these functions.

To check non-destructively whether an exception is currently set, use [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred). It gives back the active exception object, or `NULL` when nothing has been raised. Ordinarily there’s no reason to invoke `PyErr_Occurred()` to learn whether a call failed, since the return value should already tell you.

Suppose a function *f* invokes another function *g* and notices that *g* has failed; *f* ought to return an error value of its own (usually `NULL` or `-1`). It should *not* invoke any `PyErr_*` function — *g* already did that. *f*’s caller then likewise passes an error indication up to *its* own caller, again *without* invoking `PyErr_*`, and onward — the function that first noticed the trouble already reported the most precise cause. As soon as the error arrives at the Python interpreter’s main loop, it halts the Python code now running and looks for an exception handler the Python programmer arranged.

(In some situations a module really can produce a more precise error message by invoking a second `PyErr_*` function, and doing so there is perfectly acceptable. Generally speaking, though, this isn’t needed and risks discarding details about why the error happened: most operations have several possible failure modes.)

If you want to disregard an exception that a failed call set, you have to clear the exception condition deliberately by invoking [`PyErr_Clear()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Clear). C code ought to invoke `PyErr_Clear()` only when it doesn’t intend to forward the error to the interpreter but instead means to deal with it entirely on its own (perhaps by attempting an alternative, or carrying on as though nothing happened).

Each failed `malloc()` call has to become an exception — whoever directly calls `malloc()` (or `realloc()`) must invoke [`PyErr_NoMemory()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NoMemory) and itself return a failure indicator. Since every object-creating function (for instance [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong)) already handles this, this remark applies solely to anyone calling `malloc()` directly.

Note as well that, apart from the notable case of [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and its relatives, functions returning an integer status generally hand back a positive value or zero on success and `-1` on failure, much like Unix system calls.

Lastly, take care to tidy up garbage (by issuing [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) or [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) calls on objects you already built) whenever you return an error indicator!

Deciding which exception to raise is left completely to you. Pre-declared C objects exist for all the built-in Python exceptions — [`PyExc_ZeroDivisionError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_ZeroDivisionError) among them — and you may use them directly. Naturally, pick your exceptions sensibly — don’t reach for [`PyExc_TypeError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_TypeError) to signal that a file wouldn’t open (that scenario probably calls for [`PyExc_OSError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_OSError)). When the trouble lies in the argument list, the [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) function ordinarily raises `PyExc_TypeError`. When an argument’s value has to fall in a specific range or meet some other condition, [`PyExc_ValueError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_ValueError) fits.

You can likewise declare a fresh exception belonging only to your module. The most straightforward route is to set up a static global object variable near the top of the file:

```c
static PyObject *SpamError = NULL;

```

and give it a value by invoking [`PyErr_NewException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewException) inside the module’s [`Py_mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function (`spam_module_exec()`):

```c
SpamError = PyErr_NewException("spam.error", NULL, NULL);

```

Because `SpamError` is a global variable, each module reinitialization — that is, every time the [`Py_mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function runs — overwrites it.

For the time being, let’s sidestep that problem: we will prevent repeated initialization by raising an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError):

```c
static PyObject *SpamError = NULL;

static int
spam_module_exec(PyObject *m)
{
    if (SpamError != NULL) {
        PyErr_SetString(PyExc_ImportError,
                        "cannot initialize spam module more than once");
        return -1;
    }
    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    if (PyModule_AddObjectRef(m, "SpamError", SpamError) < 0) {
        return -1;
    }

    return 0;
}

static PyModuleDef_Slot spam_module_slots[] = {
    {Py_mod_exec, spam_module_exec},
    {0, NULL}
};

static struct PyModuleDef spam_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "spam",
    .m_size = 0,  // non-negative
    .m_slots = spam_module_slots,
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModuleDef_Init(&spam_module);
}

```

[Subject index](INDEX.md) · [Previous source section](a-simple-example-pyobject-pyarg-parsetuple-pylong-fromlong.md) · [Next source section](intermezzo-errors-and-exceptions-and-pylong-fromlong.md)
