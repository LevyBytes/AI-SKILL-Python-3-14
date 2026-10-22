# Python 3.13.0 alpha 5 / core and builtins / exceptions

[gh-116604](https://github.com/python/cpython/issues/116604): Honor the garbage collector's state when indirect calls go through [`PyErr_CheckSignals()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_CheckSignals) and the evaluation breaker. Patch by Pablo Galindo

[gh-115823](https://github.com/python/cpython/issues/115823): Compute error ranges properly in the parser when it raises [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions triggered by invalid byte sequences. Patch by Pablo Galindo

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
