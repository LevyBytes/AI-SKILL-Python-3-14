# interpreter lifecycle C API: Initialization prerequisites and preinitialization-safe APIs

### Before Python initialization

When you embed Python inside an application, you must invoke `Py_Initialize()` ahead of any other Python/C API call, aside from a small set of functions and the global configuration variables.

These functions are safe to invoke while Python is still uninitialized:

- Functions that initialize the interpreter:

  - `Py_Initialize()`

  - `Py_InitializeEx()`

  - `Py_InitializeFromConfig()`

  - `Py_BytesMain()`

  - `Py_Main()`

  - the runtime pre-initialization functions covered in [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config)

- Configuration functions:

  - [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab)

  - [`PyImport_ExtendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ExtendInittab)

  - `PyInitFrozenExtensions()`

  - [`PyMem_SetAllocator()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetAllocator)

  - [`PyMem_SetupDebugHooks()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetupDebugHooks)

  - [`PyObject_SetArenaAllocator()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_SetArenaAllocator)

  - `Py_SetProgramName()`

  - `Py_SetPythonHome()`

  - the configuration functions covered in [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config)

- Informative functions:

  - `Py_IsInitialized()`

  -

[Subject index](INDEX.md) · [Previous source contract](interpreter-initialization-and-finalization.md) · [Following source contract](pymem-getallocator-to-pymutex-unlock.md)
