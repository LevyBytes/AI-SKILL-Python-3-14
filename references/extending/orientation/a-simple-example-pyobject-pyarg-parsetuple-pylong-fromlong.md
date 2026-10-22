# A Simple Example — PyObject, PyArg_ParseTuple, PyLong_FromLong

`<stdio.h>`

- `<stdlib.h>`

- `<string.h>`

What we append next to the module file is the C function that fires when Python evaluates the expression `spam.system(string)` (the mechanism that triggers the call follows shortly):

```c
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}

```

Mapping the Python argument list (say, the lone expression `"ls -l"`) onto the arguments handed to the C function is direct. By convention the C function always carries two arguments, named *self* and *args*.

For module-level functions the *self* argument refers to the module object; in the case of a method it would refer to the object instance instead.

A pointer to a Python tuple object holding the arguments is what the *args* argument supplies. Every entry within that tuple lines up with one argument from the call’s argument list. Because these arguments are Python objects, our C function has to translate them into C values before it can do anything with them. The Python API supplies [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple), which validates the argument types and turns them into C values. A template string drives it, fixing both the argument types it demands and the C variable types where the converted results land. We return to this topic later.

When all arguments carry the correct type and their pieces have been deposited into the variables whose addresses you handed over, [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) yields true (nonzero). Should an invalid argument list arrive, it yields false (zero). On that path it additionally raises a suitable exception, letting the caller return `NULL` right away (just as the example showed).

[Subject index](INDEX.md) · [Previous source section](a-simple-example-py-ssize-t-py-limited-api.md) · [Next source section](intermezzo-errors-and-exceptions-and-pymoduledef-init.md) · [Owning section and setup](a-simple-example-py-ssize-t-py-limited-api.md)
