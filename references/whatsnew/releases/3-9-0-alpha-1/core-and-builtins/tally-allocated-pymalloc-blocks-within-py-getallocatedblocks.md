# Python 3.9.0 alpha 1 / core and builtins / tally allocated pymalloc blocks within py getallocatedblocks

[bpo-37537](https://bugs.python.org/issue?@action=redirect&bpo=37537): Tally the allocated pymalloc blocks within _Py_GetAllocatedBlocks(). Doing so slows _Py_GetAllocatedBlocks() down yet hands a minor speedup to _PyObject_Malloc() and _PyObject_Free().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
