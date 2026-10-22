# Extending Python with C or C++

### 1. Extending Python with C or C++

Adding fresh built-in modules to Python is reasonably simple, provided you have C programming experience. These *extension modules* unlock two capabilities that pure Python cannot offer on its own: they can define brand-new built-in object types, and they can invoke C library routines together with system calls.

The Python API (Application Programmers Interface) exposes a collection of functions, macros and variables that reach into nearly every corner of the Python run-time system, and extensions rely on it. A C source file gains access to the Python API by pulling in the header `"Python.h"`.

How you compile an extension module hinges both on what you plan to do with it and on how your system is configured; the specifics appear in chapters further on.

Note

CPython is the only implementation that the C extension interface targets, so extension modules will not run under other Python implementations. There are plenty of scenarios where you can sidestep C extensions entirely and stay portable across implementations. As an illustration, when your goal is to invoke C library functions or system calls, prefer the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module or the [cffi](https://cffi.readthedocs.io/) library over hand-rolling C code. With those modules you describe the interface to C code from within Python itself, which travels far better across Python implementations than authoring and building a C extension module would.

[Subject index](INDEX.md) · [Next source section](a-simple-example-py-ssize-t-py-limited-api.md)
