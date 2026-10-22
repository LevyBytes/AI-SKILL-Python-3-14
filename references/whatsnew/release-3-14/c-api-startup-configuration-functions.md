# Python 3.14 changes: Startup configuration functions and option access

[`PyConfig_Names()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Names)

(Contributed by Victor Stinner in [gh-107954](https://github.com/python/cpython/issues/107954).)

- Introduce functions for configuring Python startup (PEP 741: Python configuration C API):

  - [`Py_InitializeFromInitConfig()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_InitializeFromInitConfig)

  - [`PyInitConfig_AddModule()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_AddModule)

  - [`PyInitConfig_Create()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_Create)

  - [`PyInitConfig_Free()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_Free)

  - [`PyInitConfig_FreeStrList()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_FreeStrList)

  - [`PyInitConfig_GetError()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetError)

  - [`PyInitConfig_GetExitCode()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetExitCode)

  - [`PyInitConfig_GetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetInt)

  - [`PyInitConfig_GetStr()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetStr)

  - [`PyInitConfig_GetStrList()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetStrList)

  - [`PyInitConfig_HasOption()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_HasOption)

  - [`PyInitConfig_SetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_SetInt)

  - [`PyInitConfig_SetStr()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_SetStr)

  - [`PyInitConfig_SetStrList()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_SetStrList)

(Contributed by Victor Stinner in [gh-107954](https://github.com/python/cpython/issues/107954).)

- Introduce the [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen) function for opening a file. It behaves much like the standard C `fopen()` routine, but takes a Python object for the *path* argument and raises an exception when something goes wrong. To close the file, use the matching new [`Py_fclose()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fclose) function. (Contributed by Victor Stinner in [gh-127350](https://github.com/python/cpython/issues/127350).)

- Introduce [`Py_HashBuffer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashBuffer), which computes and yields a buffer's hash value. (Contributed by Antoine Pitrou and Victor Stinner in [gh-122854](https://github.com/python/cpython/issues/122854).)

- Introduce the [`PyImport_ImportModuleAttr()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleAttr) and [`PyImport_ImportModuleAttrString()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleAttrString) helpers, each of which imports a module and then fetches one of its attributes. (Contributed by Victor Stinner in [gh-128911](https://github.com/python/cpython/issues/128911).)

-

[Subject index](INDEX.md) · [Next source section](iterator-results-and-monitoring-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-additions.md) · [Preceding release/subject continuation](c-api-additions.md)
