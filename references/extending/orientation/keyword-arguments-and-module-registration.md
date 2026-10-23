# Keyword Parameters for Extension Functions - PyArg_ParseTupleAndKeywords, PyObject, PyArg_ParseTuple, Py_RETURN_NONE, PyMethodDef, PyCFunction, PyModuleDef, PyModuleDef_HEAD_INIT, PyMODINIT_FUNC, PyInit_keywdarg, PyModuleDef_Init

### 1.8. Keyword Parameters for Extension Functions

The [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) function carries the following declaration:

```c
int PyArg_ParseTupleAndKeywords(PyObject *arg, PyObject *kwdict,
                                const char *format, char * const *kwlist, ...);

```

The *arg* and *format* parameters match those of the [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) function exactly. As for *kwdict*, that parameter carries the keyword dictionary that the Python runtime supplies in third position. A `NULL`-terminated roster of strings naming the parameters constitutes *kwlist*; these names get paired with the type information drawn from *format*, working left to right. When it succeeds, [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) returns true; otherwise it returns false and raises a suitable exception.

Note

Nested tuples are unparseable once keyword arguments are in play! Any keyword parameters supplied that aren't listed in *kwlist* will trigger a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

What follows is a sample module that employs keywords, derived from an example by Geoff Philbrick ([philbrick@hks.com](mailto:philbrick%40hks.com)):

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
keywdarg_parrot(PyObject *self, PyObject *args, PyObject *keywds)
{
    int voltage;
    const char *state = "a stiff";
    const char *action = "voom";
    const char *type = "Norwegian Blue";

    static char *kwlist[] = {"voltage", "state", "action", "type", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, keywds, "i|sss", kwlist,
                                     &voltage, &state, &action, &type))
        return NULL;

    printf("-- This parrot wouldn't %s if you put %i Volts through it.\n",
           action, voltage);
    printf("-- Lovely plumage, the %s -- It's %s!\n", type, state);

    Py_RETURN_NONE;
}

static PyMethodDef keywdarg_methods[] = {
    /* The cast of the function is necessary since PyCFunction values
     * only take two PyObject* parameters, and keywdarg_parrot() takes
     * three.
     */
    {"parrot", (PyCFunction)(void(*)(void))keywdarg_parrot, METH_VARARGS | METH_KEYWORDS,
     "Print a lovely skit to standard output."},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

static struct PyModuleDef keywdarg_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "keywdarg",
    .m_size = 0,
    .m_methods = keywdarg_methods,
};

PyMODINIT_FUNC
PyInit_keywdarg(void)
{
    return PyModuleDef_Init(&keywdarg_module);
}

```

[Subject index](INDEX.md) · [Previous source section](complex-extension-argument-parsing.md) · [Next source section](building-return-values.md)
