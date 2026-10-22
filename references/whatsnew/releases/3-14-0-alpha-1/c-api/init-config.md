# Python 3.14.0 alpha 1 / c api / init config

[gh-107954](https://github.com/python/cpython/issues/107954): Introduce functions for configuring Python initialization ([**PEP 741**](https://peps.python.org/pep-0741/)):

  - [`PyInitConfig_Create()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_Create)

  - [`PyInitConfig_Free()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_Free)

  - [`PyInitConfig_GetError()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetError)

  - [`PyInitConfig_GetExitCode()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetExitCode)

  - [`PyInitConfig_HasOption()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_HasOption)

  - [`PyInitConfig_GetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetInt)

  - [`PyInitConfig_GetStr()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetStr)

  - [`PyInitConfig_GetStrList()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_GetStrList)

  - [`PyInitConfig_FreeStrList()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_FreeStrList)

  - [`PyInitConfig_SetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_SetInt)

  - [`PyInitConfig_SetStr()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyInitConfig_SetStr)

[gh-107954](https://github.com/python/cpython/issues/107954): Introduce functions that read and write the live runtime Python configuration:

  - [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get)

  - [`PyConfig_GetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_GetInt)

  - [`PyConfig_Set()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Set)

  - [`PyConfig_Names()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Names)

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
