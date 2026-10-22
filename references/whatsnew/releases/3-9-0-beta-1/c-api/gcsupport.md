# Python 3.9.0 beta 1 / c api / gcsupport

[bpo-40428](https://bugs.python.org/issue?@action=redirect&bpo=40428): The functions listed below were dropped from the C API. Invoke [`PyGC_Collect()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Collect) directly to release every free list.

  - `PyAsyncGen_ClearFreeLists()`

  - `PyContext_ClearFreeList()`

  - `PyDict_ClearFreeList()`

  - `PyFloat_ClearFreeList()`

  - `PyFrame_ClearFreeList()`

  - `PyList_ClearFreeList()`

  - `PySet_ClearFreeList()`

  - `PyTuple_ClearFreeList()`

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
