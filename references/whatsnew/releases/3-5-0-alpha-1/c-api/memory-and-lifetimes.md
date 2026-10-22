# Python 3.5.0 alpha 1 / c api / memory and lifetimes

[bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233): Introduced these new C routines: PyMem_RawCalloc(), PyMem_Calloc(), PyObject_Calloc(), _PyObject_GC_Calloc(). For sizeable objects, bytes(int) now relies on `calloc()` rather than `malloc()`, which runs faster while consuming less memory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
