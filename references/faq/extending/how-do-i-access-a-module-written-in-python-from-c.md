# How do I access a module written in Python from C?

### How do I access a module written in Python from C?

Obtaining a pointer to the module object goes like this:

```c
module = PyImport_ImportModule("<modulename>");

```

Should the module not yet have been imported (that is, it has yet to show up in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules)), this brings it to life; if it already exists, the call merely returns whatever `sys.modules["<modulename>"]` holds. Take note that it never places the module into any namespace — all it guarantees is that the module has been initialized and now resides in `sys.modules`.

From there, reaching the module's attributes — meaning any name the module defines — works like this:

```c
attr = PyObject_GetAttrString(module, "<attrname>");

```

Assigning to variables inside the module via [`PyObject_SetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttrString) is equally valid.

[Subject index](INDEX.md)
