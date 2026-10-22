# The None Object

## The None Object

### The `None` Object

Bear in mind that the [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) belonging to `None` is not made directly available through the Python/C API. Because `None` is a singleton, a plain object-identity check (in C, `==`) does the job. For that very reason no `PyNone_Check()` function exists.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_None

The Python `None` object, which stands for the absence of a value. It carries no methods and is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

Changed in version 3.12: `Py_None` is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

 Py_RETURN_NONE

Hand `Py_None` back as a function's return value.

[Subject index](INDEX.md) · [Previous source contract](../monitoring-c-api/pymonitoring-enterscope-to-pymonitoring-exitscope.md)
