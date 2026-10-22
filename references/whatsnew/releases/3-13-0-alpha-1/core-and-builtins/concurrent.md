# Python 3.13.0 alpha 1 / core and builtins / concurrent

[gh-105699](https://github.com/python/cpython/issues/105699): An uncommon race while assigning `Py_FileSystemDefaultEncoding` and `Py_FileSystemDefaultEncodeErrors` (both deprecated) during the concurrent startup of two isolated subinterpreters no longer crashes Python. These are henceforth assigned only over the course of runtime startup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
