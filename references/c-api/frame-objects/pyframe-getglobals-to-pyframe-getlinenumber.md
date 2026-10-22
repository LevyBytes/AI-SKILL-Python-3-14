# frame objects C API: `PyFrame_GetGlobals()`, `PyFrame_GetLasti()`, `PyFrame_GetVar()`, `PyFrame_GetVarString()`, `PyFrame_GetLocals()`, `PyFrame_GetLineNumber()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetGlobals(PyFrameObject *frame)

*Return value: New reference.*

Obtain the [`f_globals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_globals) attribute of *frame*.

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference). What comes back is never `NULL`.

Added in version 3.11.

 int PyFrame_GetLasti(PyFrameObject *frame)

Obtain the [`f_lasti`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lasti) attribute of *frame*.

Hands back -1 where `frame.f_lasti` is `None`.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetVar(PyFrameObject *frame, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.*

Obtain the variable *name* out of *frame*.

- On success, hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing at the variable's value.

- Where the variable is absent, raise [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) and hand back `NULL`.

- On error, raise an exception and hand back `NULL`.

The *name* type has to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

Added in version 3.12.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetVarString(PyFrameObject *frame, const char *name)

*Return value: New reference.*

Much like `PyFrame_GetVar()`, except the variable name arrives as a C string encoded in UTF-8.

Added in version 3.12.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetLocals(PyFrameObject *frame)

*Return value: New reference.*

Obtain the [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) attribute of *frame*. Where the frame points at an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope), this hands back a write-through proxy object through which the locals can be altered. Under every other circumstance (classes, modules, [`exec()`](https://docs.python.org/3.14/library/functions.html#exec), [`eval()`](https://docs.python.org/3.14/library/functions.html#eval)) it hands back the mapping that stands for the frame locals directly (just as laid out for [`locals()`](https://docs.python.org/3.14/library/functions.html#locals)).

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

Added in version 3.11.

Changed in version 3.13: Under [**PEP 667**](https://peps.python.org/pep-0667/), hand back an instance of `PyFrameLocalsProxy_Type`.

 int PyFrame_GetLineNumber(PyFrameObject *frame)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Hand back whichever line number *frame* happens to be running right now.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyframeobject-to-pyframe-getgenerator.md) · [Following source contract](pyframelocalsproxy-type-to-pyframelocalsproxy-check.md)
