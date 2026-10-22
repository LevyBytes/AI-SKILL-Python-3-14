# Python 3.14 changes: Version packing, byte joins and runtime configuration

### New features in the C API

- Introduce [`Py_PACK_VERSION()`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_PACK_VERSION) and [`Py_PACK_FULL_VERSION()`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_PACK_FULL_VERSION), a pair of new macros that bit-pack Python version numbers. They come in handy when comparing against [`Py_Version`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_Version) or [`PY_VERSION_HEX`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.PY_VERSION_HEX). (Contributed by Petr Viktorin in [gh-128629](https://github.com/python/cpython/issues/128629).)

- Introduce the [`PyBytes_Join(sep, iterable)`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Join) function, the analog of `sep.join(iterable)` over in Python. (Contributed by Victor Stinner in [gh-121645](https://github.com/python/cpython/issues/121645).)

- Introduce functions for adjusting the configuration of the running Python interpreter (PEP 741: Python configuration C API):

  - [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get)

  - [`PyConfig_GetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_GetInt)

  - [`PyConfig_Set()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Set)

  -

[Subject index](INDEX.md) · [Previous source section](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Following release/subject continuation](c-api-startup-configuration-functions.md)
