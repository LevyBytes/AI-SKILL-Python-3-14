# Docstring macros

### Docstring macros

 PyDoc_STRVAR(name, str)

Builds a variable named *name* suitable for use within docstrings. Should Python be compiled with docstrings turned off ([`--without-doc-strings`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-doc-strings)), the value comes out as an empty string.

Example:

```c
PyDoc_STRVAR(pop_doc, "Remove and return the rightmost element.");

static PyMethodDef deque_methods[] = {
    // ...
    {"pop", (PyCFunction)deque_pop, METH_NOARGS, pop_doc},
    // ...
}

```

Expands to `PyDoc_VAR(*name*) = PyDoc_STR(*str*)`.

 PyDoc_STR(str)

Expands to whatever input string you give it, or to an empty string when docstrings have been switched off ([`--without-doc-strings`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-doc-strings)).

Example:

```c
static PyMethodDef pysqlite_row_methods[] = {
    {"keys", (PyCFunction)pysqlite_row_keys, METH_NOARGS,
        PyDoc_STR("Returns the keys of the row.")},
    {NULL, NULL}
};

```

 PyDoc_VAR(name)

Declares a static character array variable bearing the supplied *name*. Expands to `static const char *name*[]`

For example:

```c
PyDoc_VAR(python_doc) = PyDoc_STR(
   "A genus of constricting snakes in the Pythonidae family native "
   "to the tropics and subtropics of the Eastern Hemisphere.");

```

[Subject index](INDEX.md) · [Previous source contract](py-can-start-threads-to-py-getenv.md) · [Following source contract](py-unused-to-py-gcc-attribute.md)
