# Python 3.14.0 beta 2 / c api / subinterpreters

[gh-134144](https://github.com/python/cpython/issues/134144): Repair the crash triggered by calling [`Py_EndInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_EndInterpreter) using a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) other than the interpreter's initial thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
