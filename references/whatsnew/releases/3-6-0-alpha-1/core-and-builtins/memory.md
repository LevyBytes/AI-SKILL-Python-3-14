# Python 3.6.0 alpha 1 / core and builtins / memory

[bpo-26249](https://bugs.python.org/issue?@action=redirect&bpo=26249): Within the [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) domain ([`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM)), the memory functions reach for the [pymalloc allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) in place of the system `malloc()`. Code that invokes `PyMem_Malloc()` while the GIL is not held may now crash; set the `PYTHONMALLOC=debug` environment variable to check that your program is using the memory allocators correctly.

[bpo-26563](https://bugs.python.org/issue?@action=redirect&bpo=26563): Should any function from the [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) family run while the GIL is not held, the debug hooks on Python memory allocators now trigger a fatal error.

[bpo-26558](https://bugs.python.org/issue?@action=redirect&bpo=26558): For the Python memory allocator [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc), its debug hooks can now spot the case where functions get called while the GIL is not held.

[bpo-26516](https://bugs.python.org/issue?@action=redirect&bpo=26516): Even on a Python that was compiled in release mode, the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetupDebugHooks) function is now usable too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
