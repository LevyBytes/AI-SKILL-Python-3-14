# Python 3.14.4 final / core and builtins / ctypes

[gh-144563](https://github.com/python/cpython/issues/144563): Corrects how the Tachyon profiler interacts with [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) plus other modules that load the Python shared library (when present) inside an independent map, since this had been confusing the mechanism responsible for loading the binary information. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
