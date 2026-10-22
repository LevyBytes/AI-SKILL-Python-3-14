# Python 3.12.0 alpha 6 / core and builtins / imports and modules

[gh-98627](https://github.com/python/cpython/issues/98627): Once an interpreter has been configured to check (and not otherwise), importing an extension module will now fail if the extension lacks support for multiple interpreters (that is, it does not implement PEP 489 multi-phase init). Neither the main interpreter nor subinterpreters built with `Py_NewInterpreter()` are affected by this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
