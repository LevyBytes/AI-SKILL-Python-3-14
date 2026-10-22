# Python 3.14.0 alpha 4 / c api / sys

[gh-128400](https://github.com/python/cpython/issues/128400): To avoid crashes, [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) stops dumping every thread on the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[gh-127350](https://github.com/python/cpython/issues/127350): Provide a [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen) function for opening files. It resembles `fopen()`, except the *path* argument is a Python object and any failure sets an exception. A companion [`Py_fclose()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fclose) function for closing files is also provided, since Windows needs it. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
