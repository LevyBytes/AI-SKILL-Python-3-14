# Python 3.12.0 alpha 2 / c api / subprocess

[gh-98610](https://github.com/python/cpython/issues/98610): A few of the configurable powers granted to sub-interpreters have shifted. Subprocesses ([`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess)) are now always permitted, where previously they could be selectively forbidden for a given sub-interpreter. In their place, `os.exec()` can now be forbidden. Forbidding daemon threads has become supported. Forbidding every thread remains permitted, though it is never the default. Keep in mind that the optional restrictions reach you solely through `_Py_NewInterpreterFromConfig()`, which is not a public API. None of this touches the main interpreter, nor does it touch [`Py_NewInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreter).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
