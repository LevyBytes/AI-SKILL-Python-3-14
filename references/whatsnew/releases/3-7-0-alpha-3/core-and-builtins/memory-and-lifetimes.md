# Python 3.7.0 alpha 3 / core and builtins / memory and lifetimes

[bpo-32096](https://bugs.python.org/issue?@action=redirect&bpo=32096): Backs out the memory allocator rework in the C API: the structures move back out of _PyRuntime and into Objects/obmalloc.c. Because the allocators are again set up statically, both PyMem_RawMalloc() and Py_DecodeLocale() may run prior to _PyRuntime_Initialize().

[bpo-30696](https://bugs.python.org/issue?@action=redirect&bpo=30696): Stops the interactive interpreter from spinning forever once memory runs out.

[bpo-30817](https://bugs.python.org/issue?@action=redirect&bpo=30817): `PyErr_PrintEx()` now clears the ignored exception that `_PySys_SetObjectId()` might raise, such as when memory is exhausted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
