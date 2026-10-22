# Python 3.14.0 alpha 5 / library / ctypes

[gh-129502](https://github.com/python/cpython/issues/129502): Rare failures while assembling the arguments for a [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) callback now follow the same path as failures raised inside the callback or while converting its result — they route through [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) rather than [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook), and they no longer populate [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc) or the related variables.

[gh-119349](https://github.com/python/cpython/issues/119349): Provide the [`ctypes.util.dllist()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.dllist) function, which enumerates the shared libraries loaded by the current process.

[gh-128156](https://github.com/python/cpython/issues/128156): With the macOS system `libffi`, [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) support for complex types is now verified at runtime (requiring macOS 10.15 or newer). Those types must additionally exist at build time.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
