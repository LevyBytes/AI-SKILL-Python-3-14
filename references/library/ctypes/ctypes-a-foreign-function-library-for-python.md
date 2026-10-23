# ctypes`ctypes` - A foreign function library for Python

### `ctypes` - A foreign function library for Python

**Source code:** [Lib/ctypes](https://github.com/python/cpython/tree/3.14/Lib/ctypes)

---

`ctypes` is a foreign function library for Python. It supplies data types that are compatible with C and lets you invoke functions inside DLLs or shared libraries. With it, such libraries can be wrapped entirely in pure Python.

This module is an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should it be absent from your build of CPython, consult the documentation supplied by your distributor — that is, whoever handed Python to you. And if you happen to be the distributor yourself, refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

Warning

`ctypes` grants low-level reach into native libraries and into the memory of the process itself, sidestepping the safety guarantees Python normally enforces and permitting arbitrary native code to run. Mistakes can corrupt data and objects, leak confidential information, trigger crashes, or otherwise undermine the integrity of the running process.

[Subject index](INDEX.md) · [Continue](ctypes-tutorial.md)
