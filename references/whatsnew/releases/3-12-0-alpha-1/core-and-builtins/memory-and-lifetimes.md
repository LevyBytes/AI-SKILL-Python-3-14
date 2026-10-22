# Python 3.12.0 alpha 1 / core and builtins / memory and lifetimes

[gh-96572](https://github.com/python/cpython/issues/96572): Repair a use after free in the trace refs build mode. Kumar Aditya wrote the patch.

[gh-97002](https://github.com/python/cpython/issues/97002): Resolve a situation where multiple frame objects might share one underlying interpreter frame, which risked corrupting memory and crashing the interpreter outright.

[gh-95876](https://github.com/python/cpython/issues/95876): Repair the format string inside `_PyPegen_raise_error_known_location` that could corrupt memory on certain 64bit systems. The function had been assembling a tuple using `i` (int) where Py_ssize_t arguments call for `n` (Py_ssize_t).

[gh-95355](https://github.com/python/cpython/issues/95355): `_PyPegen_Parser_New` now correctly spots token memory allocation errors. Honglin Zhu wrote the patch.

[gh-93252](https://github.com/python/cpython/issues/93252): Resolves a case that let internal frames survive past failed Python function calls, which could leak memory or hard-crash the interpreter.

[gh-92955](https://github.com/python/cpython/issues/92955): Corrects a memory leak in the lines and positions iterators of a code object, which went unfinalized at exit. Kumar Aditya wrote the patch.

[gh-92804](https://github.com/python/cpython/issues/92804): Corrects a memory leak in the `memoryview` iterator, which was left unfinalized at exit. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
