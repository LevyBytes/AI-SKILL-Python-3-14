# Python 3.12 changes: Per-interpreter GIL configuration and opaque reference counting

> Whatsnew reference. Wording rephrased; identifiers kept exactly as published.

[**PEP 684**](https://peps.python.org/pep-0684/): Adds the brand-new [`Py_NewInterpreterFromConfig()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreterFromConfig) function plus [`PyInterpreterConfig`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterConfig); together these let you spin up sub-interpreters that each carry their own GIL. (Consult PEP 684: A Per-Interpreter GIL for the full story.) (Contributed by Eric Snow in [gh-104110](https://github.com/python/cpython/issues/104110).)

- Within the limited C API at version 3.12, the [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) plus [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) routines are henceforth shipped as opaque calls so that their inner workings stay hidden. (Contributed by Victor Stinner in [gh-105387](https://github.com/python/cpython/issues/105387).)

[Subject index](INDEX.md) · [Next source section](c-api-changes-porting-to-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Preceding release/subject continuation](c-api-changes-new-features.md)
