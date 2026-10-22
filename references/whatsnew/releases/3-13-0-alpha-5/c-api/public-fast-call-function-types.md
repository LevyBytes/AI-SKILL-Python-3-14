# Python 3.13.0 alpha 5 / c api / public fast call function types

[gh-114626](https://github.com/python/cpython/issues/114626): Reinstate the `_PyCFunctionFastWithKeywords` name that was dropped by accident in Python 3.13 alpha 4. The old private `_PyCFunctionFastWithKeywords` name (Python 3.7) is retained as an alias pointing at the new public `PyCFunctionFastWithKeywords` name (Python 3.13a4). Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
