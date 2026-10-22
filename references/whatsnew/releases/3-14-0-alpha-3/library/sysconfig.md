# Python 3.14.0 alpha 3 / library / sysconfig

[gh-126789](https://github.com/python/cpython/issues/126789): Repaired [`sysconfig.get_config_vars()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_vars), [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths), and their siblings, which had been handing back stale cached values whenever [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) or [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) was altered. Reassigning `sys.prefix` or `sys.exec_prefix` remains inadvisable, since it can disrupt other portions of the code.

[gh-127429](https://github.com/python/cpython/issues/127429): Repaired a defect under which cross-builds produced the [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) POSIX data using the host Python's `Makefile`. That data now comes from the `Makefile` of the build in progress.

[gh-127178](https://github.com/python/cpython/issues/127178): The standard library directory now includes a `_sysconfig_vars_(...).json` file. That file holds the [`sysconfig.get_config_vars()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_vars) output for the default environment, serialized as JSON. It counts as an implementation detail and is subject to change at any moment.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
