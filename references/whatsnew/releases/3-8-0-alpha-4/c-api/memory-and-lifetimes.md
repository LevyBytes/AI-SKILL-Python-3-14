# Python 3.8.0 alpha 4 / c api / memory and lifetimes

[bpo-36763](https://bugs.python.org/issue?@action=redirect&bpo=36763): Close a memory leak in `Py_SetStandardStreamEncoding()`: free the memory whenever the function gets invoked a second time.

[bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810): Alter `PyObject_Init` so that it properly bumps the refcount of heap-allocated Type objects. Likewise repair the refcounts of heap-allocated types that were either bumping them by hand or failing to drop the type's refcount within tp_dealloc

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
