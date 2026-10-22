# Exception and warning types

### Exception and warning types

Every built-in Python exception and warning category is exposed as a global variable named `PyExc_` plus the exception's Python name. Each one carries the type [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, and each is a class object.

The full set of variables is listed here:

[Subject index](INDEX.md) · [Previous source contract](py-enterrecursivecall-to-sys-setrecursionlimit.md) · [Following source contract](exception-types.md)
