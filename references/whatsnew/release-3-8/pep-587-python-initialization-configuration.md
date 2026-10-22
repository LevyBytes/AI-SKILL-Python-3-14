# What’s New In Python 3.8 / PEP 587: Python Initialization Configuration

### PEP 587: Python Initialization Configuration

[**PEP 587**](https://peps.python.org/pep-0587/) brings a new C API for configuring Python Initialization, granting tighter control over the entire configuration along with improved error reporting.

New structures:

- [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig)

- [`PyPreConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig)

- [`PyStatus`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus)

- [`PyWideStringList`](https://docs.python.org/3.14/c-api/init_config.html#c.PyWideStringList)

New functions:

- [`PyConfig_Clear()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Clear)

- [`PyConfig_InitIsolatedConfig()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_InitIsolatedConfig)

- [`PyConfig_InitPythonConfig()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_InitPythonConfig)

- [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read)

- [`PyConfig_SetArgv()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_SetArgv)

- [`PyConfig_SetBytesArgv()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_SetBytesArgv)

- [`PyConfig_SetBytesString()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_SetBytesString)

- [`PyConfig_SetString()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_SetString)

- [`PyPreConfig_InitIsolatedConfig()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig_InitIsolatedConfig)

- [`PyPreConfig_InitPythonConfig()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig_InitPythonConfig)

- [`PyStatus_Error()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_Error)

- [`PyStatus_Exception()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_Exception)

- [`PyStatus_Exit()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_Exit)

- [`PyStatus_IsError()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_IsError)

- [`PyStatus_IsExit()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_IsExit)

- [`PyStatus_NoMemory()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_NoMemory)

- [`PyStatus_Ok()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus_Ok)

- [`PyWideStringList_Append()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyWideStringList_Append)

- [`PyWideStringList_Insert()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyWideStringList_Insert)

- [`Py_BytesMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_BytesMain)

- [`Py_ExitStatusException()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_ExitStatusException)

- [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig)

- [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize)

- [`Py_PreInitializeFromArgs()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitializeFromArgs)

- [`Py_PreInitializeFromBytesArgs()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitializeFromBytesArgs)

- [`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain)

The PEP additionally introduces `_PyRuntimeState.preconfig` (of [`PyPreConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig) type) and `PyInterpreterState.config` (of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) type) fields onto those internal structures. Going forward, `PyInterpreterState.config` serves as the canonical configuration, taking over from global configuration variables and assorted private variables.

The documentation sits at [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

A complete write-up appears in [**PEP 587**](https://peps.python.org/pep-0587/).

(Victor Stinner contributed this in [bpo-36763](https://bugs.python.org/issue?@action=redirect&bpo=36763).)

[Subject index](INDEX.md) · [Previous source section](pep-578-python-runtime-audit-hooks.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](pep-590-vectorcall-a-fast-calling-protocol-for-cpython.md)
