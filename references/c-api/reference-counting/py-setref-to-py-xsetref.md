# reference counting C API: `Py_SETREF()`, `Py_XSETREF()`

Py_SETREF(dst, src)

A macro that safely gives up a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to object *dst* and then points *dst* at *src*.

Just as with `Py_CLEAR()`, writing it the "obvious" way can be fatal:

```c
Py_DECREF(dst);
dst = src;

```

The safe way is:

```c
Py_SETREF(dst, src);

```

That sequencing makes *dst* point at *src* *before* the reference to *dst*'s previous value is released, so that whatever code fires as a side-effect of *dst* being torn down no longer assumes *dst* refers to a valid object.

Added in version 3.6.

Changed in version 3.12: Each argument of the macro is now evaluated just one time; whenever an argument brings side effects, those no longer occur twice.

 Py_XSETREF(dst, src)

A variant of the `Py_SETREF` macro that calls `Py_XDECREF()` in place of `Py_DECREF()`.

Added in version 3.6.

Changed in version 3.12: The macro's arguments now undergo evaluation one time apiece; should an argument produce side effects, they will not be triggered more than once.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-refcnt-to-py-xincref.md) · [Previous source contract](py-newref-to-py-decref.md) · [Following source contract](../reflection/pyeval-getbuiltins-to-pyeval-getfuncdesc.md)
