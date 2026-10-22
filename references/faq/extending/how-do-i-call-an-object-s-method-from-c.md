# How do I call an object’s method from C?

### How do I call an object’s method from C?

The [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod) function serves to invoke any method on an object. What you supply are the object itself, the name of the method you wish to run, a format string of the sort [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) takes, and then the argument values:

```c
PyObject *
PyObject_CallMethod(PyObject *object, const char *method_name,
                    const char *arg_format, ...);

```

It applies to every object carrying methods, be they built-in or written by you. The duty falls on you to eventually [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) the value that comes back.

Say you wish to run a file object's “seek” method passing 10, 0 (with the file object pointer taken to be “f”):

```c
res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
if (res == NULL) {
        ... an exception occurred ...
}
else {
        Py_DECREF(res);
}

```

Keep in mind that, because [`PyObject_CallObject()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallObject) *always* insists on a tuple for the argument list, you pass “()” as the format to call a function that takes no arguments, and for a one-argument call you wrap that argument in parentheses, for instance “(i)”.

[Subject index](INDEX.md)
