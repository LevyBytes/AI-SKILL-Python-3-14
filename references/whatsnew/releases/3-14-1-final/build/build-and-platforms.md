# Python 3.14.1 final / build / build and platforms

[gh-141808](https://github.com/python/cpython/issues/141808): Avoid emitting the jit stencils a second time during PGO builds running on Windows.

[gh-141784](https://github.com/python/cpython/issues/141784): Repair `_remote_debugging_module.c` so it compiles on 32-bit Linux. Pulling in Python.h ahead of the system headers guarantees that `_remote_debugging_module.c` relies on the identical types (ABI) that Python does. Victor Stinner supplied this patch.

[gh-140513](https://github.com/python/cpython/issues/140513): Produce an explicit compile-time failure if `_Py_TAIL_CALL_INTERP` is turned on while either `preserve_none` or `musttail` lacks support.

[gh-140189](https://github.com/python/cpython/issues/140189): CI gained iOS builds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
