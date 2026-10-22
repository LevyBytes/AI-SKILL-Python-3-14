# Calling Python functions from C — Py_INCREF, PyObject, PyArg_ParseTuple, PyCallable_Check, PyErr_SetString, PyExc_TypeError, Py_XINCREF, Py_XDECREF, Py_None, PyObject_CallObject, Py_BuildValue, Py_DECREF, PyErr_Clear

Happily, recursive invocation of the Python interpreter is straightforward, and a standard interface exists for invoking a Python function. (I won't go into detail about feeding the Python parser a specific string as input — should that interest you, examine how the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) command line option is implemented in `Modules/main.c` within the Python source code.)

Invoking a Python function is simple. To begin with, the Python program needs some way to hand you the Python function object. You ought to expose a function (or another interface) that accomplishes this. Upon invoking that function, stash a pointer to the Python function object (take care to [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) it!) into a global variable — or anywhere else that suits you. As an illustration, the following function could belong to a module definition:

```c
static PyObject *my_callback = NULL;

static PyObject *
my_set_callback(PyObject *dummy, PyObject *args)
{
    PyObject *result = NULL;
    PyObject *temp;

    if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
        if (!PyCallable_Check(temp)) {
            PyErr_SetString(PyExc_TypeError, "parameter must be callable");
            return NULL;
        }
        Py_XINCREF(temp);         /* Add a reference to new callback */
        Py_XDECREF(my_callback);  /* Dispose of previous callback */
        my_callback = temp;       /* Remember new callback */
        /* Boilerplate to return "None" */
        Py_INCREF(Py_None);
        result = Py_None;
    }
    return result;
}

```

You need to register this function with the interpreter via the [`METH_VARARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_VARARGS) flag, as covered in the section The Module's Method Table and Initialization Function. Documentation for the [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) function along with its arguments appears in the section Extracting Parameters in Extension Functions.

The [`Py_XINCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XINCREF) and [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) macros raise/lower an object's reference count and remain safe even when handed `NULL` pointers (though here *temp* won't actually be `NULL`). The section Reference Counts covers them in greater depth.

Afterward, once the moment arrives to invoke the function, you call the C function [`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject). It accepts two arguments, each a pointer to an arbitrary Python object: the Python function itself, plus the argument list. That argument list is required to be a tuple object, with a length equal to the count of arguments. If you wish to invoke the Python function without any arguments, hand it `NULL` or an empty tuple; for a single-argument call, supply a singleton tuple. [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) yields a tuple whenever its format string holds zero or more format codes enclosed in parentheses. Consider this:

```c
int arg;
PyObject *arglist;
PyObject *result;
...
arg = 123;
...
/* Time to call the callback */
arglist = Py_BuildValue("(i)", arg);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);

```

[`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject) hands back a Python object pointer: this represents the Python function's return value. With regard to its arguments, `PyObject_CallObject()` is "reference-count-neutral". The example built a fresh tuple to act as the argument list, and that tuple is [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF)-ed right after the `PyObject_CallObject()` call completes.

Whatever [`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject) returns counts as "new": either a freshly minted object, or a pre-existing one whose reference count got bumped. Consequently, unless you intend to keep it in a global variable, you ought to [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) the result somehow, even (and indeed especially!) when its value holds no interest for you.

Prior to doing so, though, you must confirm the return value is not `NULL`. A `NULL` value means the Python function ended by raising an exception. Should the C code invoking [`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject) itself have been called from Python, it ought now to hand an error signal back to its Python caller, letting the interpreter print a stack trace or letting the calling Python code deal with the exception. When that's neither feasible nor wanted, clear the exception by calling [`PyErr_Clear()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Clear). Consider:

```c
if (result == NULL)
    return NULL; /* Pass error back */
...use result...
Py_DECREF(result);

```

Based on the interface you want for the Python callback function, you might additionally need to supply an argument list to [`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject). At times the Python program furnishes the argument list too, by way of the same interface that named the callback function. That list can then be stored and reused exactly as the function object is. In other situations, you might need to assemble a fresh tuple for use as the argument list. The easiest route to that is calling [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue). For instance, to pass along an integral event code, the code below would serve:

```c
PyObject *arglist;
...
arglist = Py_BuildValue("(l)", eventcode);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);
if (result == NULL)
    return NULL; /* Pass error back */
/* Here maybe use the result */
Py_DECREF(result);

```

[Subject index](INDEX.md) · [Next source section](c-callback-keyword-arguments-and-reference-cleanup.md) · [Preceding cross-file owner and contract](calling-python-functions-from-c.md)
