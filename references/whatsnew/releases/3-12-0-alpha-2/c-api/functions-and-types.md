# Python 3.12.0 alpha 2 / c api / functions and types

[gh-98608](https://github.com/python/cpython/issues/98608): A `_PyInterpreterConfig` has been introduced, and `_Py_NewInterpreter()` now goes by the name `_Py_NewInterpreterFromConfig()`. The former "isolated_subinterpreters" argument has become a fine-grained config that preserves the earlier behavior. Bear in mind that the whole of this remains "private" API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
