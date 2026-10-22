# Python 3.11.0 beta 1 / c api / compiler and parser

[gh-91320](https://github.com/python/cpython/issues/91320): Silence C++ compiler complaints about “old-style cast” (`g++ -Wold-style-cast`) across the Python C API. Apply the C++ `reinterpret_cast<>` and `static_cast<>` casts whenever the Python C API gets used from C++. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
