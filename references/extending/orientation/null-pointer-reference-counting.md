# NULL Pointers - Py_INCREF, Py_DECREF, Py_XINCREF, Py_XDECREF, Pytype_Check

### 1.10.4. NULL Pointers

As a rule, routines that accept object references for their arguments assume you will never hand them `NULL` pointers, and they will crash (or set up a later crash) when you do. Routines handing back object references typically yield `NULL` solely to signal that an exception arose. They skip checking their arguments for `NULL` because a routine frequently forwards the objects it gets to yet another routine — were every one to verify `NULL`, the duplicated checks would pile up and slow the code down.

The preferable habit is to check for `NULL` right at the “source:” the moment you take in a pointer that might be `NULL`, say one coming back from `malloc()` or from a routine capable of raising an exception.

The [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) and [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) macros skip any `NULL` test — yet their counterparts [`Py_XINCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XINCREF) and [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) perform one.

The type-testing macros (`Pytype_Check()`) likewise omit `NULL` tests — once more, plenty of code chains several of them together to weigh an object against a handful of candidate types, and adding the check would just duplicate work. No `NULL`-aware versions of these exist.

Python's machinery for invoking C functions promises that the argument list given to them (`args` throughout the examples) is never `NULL` — indeed it promises the thing is invariably a tuple [4].

Permitting a `NULL` pointer to “escape” out to the Python user is a grave mistake.

[Subject index](INDEX.md) · [Previous source section](borrowed-references-and-implicit-calls.md) · [Next source section](writing-extensions-in-c.md)
