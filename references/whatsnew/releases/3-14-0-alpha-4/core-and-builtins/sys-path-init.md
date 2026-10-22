# Python 3.14.0 alpha 4 / core and builtins / sys path init

[gh-66409](https://github.com/python/cpython/issues/66409): Throughout the [path initialization](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init) step, the runtime now compares `base_exec_prefix` against `base_prefix` first, resorting to a scan of the Python interpreter directory only afterward.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
