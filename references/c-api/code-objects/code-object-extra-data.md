# Extra information

### Extra information

So that low-level extensions to frame evaluation — external just-in-time compilers among them — can be built, arbitrary extra data may be fastened onto code objects.

The functions here sit in the unstable C API tier: the capability is a CPython implementation detail, and its API can shift with no deprecation warnings.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnstable_Eval_RequestCodeExtraIndex([freefunc](https://docs.python.org/3.14/c-api/typeobj.html#c.freefunc) free)

 *Sits in the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); a minor release may alter it without any warning.*

Give back a fresh opaque index value that serves for adding data to code objects.

As a rule you invoke this function a single time per interpreter, then hand the result to `PyCode_GetExtra` and `PyCode_SetExtra` to work with data on individual code objects.

When *free* is not `NULL`: upon a code object's deallocation, *free* is invoked on any non-`NULL` data kept under the new index. Reach for [`Py_DecRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DecRef) where you are storing a [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

Added in version 3.6: as `_PyEval_RequestCodeExtraIndex`

Changed in version 3.12: Renamed to `PyUnstable_Eval_RequestCodeExtraIndex`. The earlier private name, now deprecated, remains usable until the API changes.

 int PyUnstable_Code_GetExtra([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, void **extra)

 *Falls within the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); minor releases can change it without warning.*

Point *extra* at the extra data held under the given index. Yield 0 when it succeeds. On failure, set an exception and yield -1.

Where the index has had no data set, point *extra* at `NULL` and yield 0 without raising any exception.

Added in version 3.6: as `_PyCode_GetExtra`

Changed in version 3.12: Renamed to `PyUnstable_Code_GetExtra`. The earlier private name, now deprecated, remains usable until the API changes.

 int PyUnstable_Code_SetExtra([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, void *extra)

 *Lives in the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); without warning, a minor release may change it.*

Make the extra data held under the given index equal to *extra*. Yield 0 when it succeeds. On failure, set an exception and yield -1.

Added in version 3.6: as `_PyCode_SetExtra`

Changed in version 3.12: Renamed to `PyUnstable_Code_SetExtra`. The earlier private name, now deprecated, remains usable until the API changes.

[Subject index](INDEX.md) · [Previous source contract](code-object-flags.md)
