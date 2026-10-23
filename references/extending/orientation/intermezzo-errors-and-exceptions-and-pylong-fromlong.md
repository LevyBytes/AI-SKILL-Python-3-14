# Intermezzo: Errors and Exceptions - PyErr_NewException, Py_DECREF, PyMODINIT_FUNC, PyErr_SetString, PyObject, PyArg_ParseTuple, PyLong_FromLong

Observe that the Python-side name of the exception object is `spam.error`. The [`PyErr_NewException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewException) function can construct a class whose base is [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) (unless you supply some other class in place of `NULL`), as covered in [Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html#bltin-exceptions).

Observe also that the `SpamError` variable holds on to a reference to the freshly built exception class; that is deliberate! Because outside code could strip the exception out of the module, holding an owned reference to the class guarantees it won’t be thrown away, which would turn `SpamError` into a dangling pointer. Were it to dangle, C code raising the exception might trigger a core dump or other unexpected behavior.

At this stage the [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) call that would drop this reference is absent. Even once the Python interpreter winds down, the global `SpamError` variable escapes garbage collection. It will “leak”. We have, nonetheless, made sure this occurs no more than once per process.

We take up the role of [`PyMODINIT_FUNC`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyMODINIT_FUNC) as a function return type further along in this example.

Your extension module can raise the `spam.error` exception through a call to [`PyErr_SetString()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetString), as illustrated below:

```c
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(SpamError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}

```

[Subject index](INDEX.md) · [Previous source section](intermezzo-errors-and-exceptions-and-pymoduledef-init.md) · [Next source section](argument-parsing-and-return-value-example.md) · [Owning section and setup](intermezzo-errors-and-exceptions-and-pymoduledef-init.md)
