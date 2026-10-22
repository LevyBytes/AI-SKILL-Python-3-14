# compileall — `compileall` — Byte-compile Python libraries

## compileall — Byte-compile Python libraries

### `compileall` — Byte-compile Python libraries

**Source code:** [Lib/compileall.py](https://github.com/python/cpython/tree/3.14/Lib/compileall.py)

---

A handful of helper routines here assist with the installation of Python libraries. They walk a directory tree and compile the Python source files inside it. A typical use is to build the cached byte-code files when a library is installed, so that they are ready to go even for users lacking write access to the library folders.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either non-functional or absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

[Subject index](INDEX.md) · [Continue](command-line-use.md)
