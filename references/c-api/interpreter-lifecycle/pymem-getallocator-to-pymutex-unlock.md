# interpreter lifecycle C API: Preinitialization-safe allocators, metadata and mutexes

[`PyMem_GetAllocator()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_GetAllocator)

  - [`PyObject_GetArenaAllocator()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_GetArenaAllocator)

  - `Py_GetBuildInfo()`

  - `Py_GetCompiler()`

  - `Py_GetCopyright()`

  - `Py_GetPlatform()`

  - `Py_GetVersion()`

  - `Py_IsInitialized()`

- Utilities:

  - [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale)

  - the status reporting and utility functions covered in [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config)

- Memory allocators:

  - [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc)

  - [`PyMem_RawRealloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawRealloc)

  - [`PyMem_RawCalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawCalloc)

  - [`PyMem_RawFree()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawFree)

- Synchronization:

  - [`PyMutex_Lock()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_Lock)

  - [`PyMutex_Unlock()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_Unlock)

Note

Although they resemble some of the entries above, the functions that follow **should not be called** until the interpreter is up and running: [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale), [`PyEval_InitThreads()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_InitThreads), and `Py_RunMain()`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-initialize-to-py-isinitialized.md) · [Following source contract](py-byteswarningflag-to-py-interactiveflag.md)
