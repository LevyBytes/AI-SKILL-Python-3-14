# Recommended third party tools

### Recommended third party tools

The third party tools listed below provide both more straightforward and more advanced routes to building C, C++ and Rust extensions for Python:

- [Cython](https://cython.org/)

- [cffi](https://cffi.readthedocs.io)

- [HPy](https://hpyproject.org/)

- [nanobind](https://github.com/wjakob/nanobind) (C++)

- [Numba](https://numba.pydata.org/)

- [pybind11](https://pybind11.readthedocs.io/) (C++)

- [PyO3](https://pyo3.rs/) (Rust)

- [SWIG](https://www.swig.org)

Adopting tools like these can spare you from writing code locked tightly to one specific CPython version, sidestep reference-counting mistakes, and let you concentrate on your own code instead of on wrangling the CPython API. Generally speaking, support for new Python releases comes via a tool update, and your code will frequently pick up newer, more efficient APIs on its own. A few of the tools can additionally compile against other Python implementations from one common source set.

The people who maintain Python don't support these projects, so any issues should be brought straight to the projects themselves. Keep in mind to confirm the project remains maintained and supported, since the list above could grow stale.

See also

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/guides/packaging-binary-extensions/)

Beyond surveying several of the available tools that ease building binary extensions, the Python Packaging User Guide also examines the assorted reasons that crafting an extension module might be worthwhile to begin with.

[Subject index](INDEX.md) · [Previous source contract](py-debug.md)
