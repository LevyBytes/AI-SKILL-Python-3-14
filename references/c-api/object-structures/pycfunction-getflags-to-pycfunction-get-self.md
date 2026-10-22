# object structures C API: `PyCFunction_GetFlags()`, `PyCFunction_GET_FLAGS()`, `PyCFunction_GetFunction()`, `PyCFunction_GET_FUNCTION()`, `PyCFunction_GetSelf()`, `PyCFunction_GET_SELF()`

int PyCFunction_GetFlags(PyObject *func)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Fetch the flags of the function on *func* exactly as they were handed to `ml_flags`.

Should *func* not be a C function object, this fails and raises an exception. *func* may not be `NULL`.

On success this function gives back the function's flags, and on failure it gives back `-1` with an exception set.

 int PyCFunction_GET_FLAGS(PyObject *func)

Behaves like `PyCFunction_GetFlags()`, but skips any error or type checking.

 PyCFunction PyCFunction_GetFunction(PyObject *func)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Fetch the function pointer on *func* exactly as it was handed to `ml_meth`.

Should *func* not be a C function object, this fails and raises an exception. *func* may not be `NULL`.

On success this function gives back the function pointer, and on failure it gives back `NULL` with an exception set.

 int PyCFunction_GET_FUNCTION(PyObject *func)

Behaves like `PyCFunction_GetFunction()`, but skips any error or type checking.

 PyObject *PyCFunction_GetSelf(PyObject *func)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Fetch the "self" object on *func*. That is the object handed to a `PyCFunction`'s first argument. With C function objects built from a `PyMethodDef` on a [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef), this turns out to be the resulting module object.

Should *func* not be a C function object, this fails and raises an exception. *func* may not be `NULL`.

On success this function gives back a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) to the "self" object, and on failure it gives back `NULL` with an exception set.

 PyObject *PyCFunction_GET_SELF(PyObject *func)

Behaves like `PyCFunction_GetSelf()`, but skips any error or type checking.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Owning structure and shared ABI conditions](pymethoddef-to-ml-doc.md) · [Previous source contract](pycmethod-type-to-pycfunction-new.md) · [Following source contract](pymemberdef-to-flags.md)
