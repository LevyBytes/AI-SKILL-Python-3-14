# Python 3.13.0 alpha 1 / library / sysconfig

[gh-88402](https://github.com/python/cpython/issues/88402): Introduce additional variables to [`sysconfig.get_config_vars()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_vars) under Windows: `LIBRARY`, `LDLIBRARY`, `LIBDIR`, `SOABI`, and `Py_NOGIL`.

[gh-110786](https://github.com/python/cpython/issues/110786): The CLI for [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) henceforth disregards [`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError), letting it terminate cleanly whenever its output feeds a pipe and that pipe shuts.

[gh-103480](https://github.com/python/cpython/issues/103480): The [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module has become a package rather than a lone single-file module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
