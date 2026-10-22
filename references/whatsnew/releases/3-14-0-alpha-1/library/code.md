# Python 3.14.0 alpha 1 / library / code

[gh-122478](https://github.com/python/cpython/issues/122478): Strip internal frames out of tracebacks displayed by [`code.InteractiveInterpreter`](https://docs.python.org/3.14/library/code.html#code.InteractiveInterpreter) under a non-default [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook). Record accurate tracebacks within [`sys.last_traceback`](https://docs.python.org/3.14/library/sys.html#sys.last_traceback) and refresh the `__traceback__` attribute on [`sys.last_value`](https://docs.python.org/3.14/library/sys.html#sys.last_value) plus [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc).

[gh-87320](https://github.com/python/cpython/issues/87320): Within [`code.InteractiveInterpreter`](https://docs.python.org/3.14/library/code.html#code.InteractiveInterpreter), trap exceptions arising from invoking a non-default [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook). Previously such an exception propagated to the caller and terminated the [REPL](https://docs.python.org/3.14/glossary.html#term-REPL).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
