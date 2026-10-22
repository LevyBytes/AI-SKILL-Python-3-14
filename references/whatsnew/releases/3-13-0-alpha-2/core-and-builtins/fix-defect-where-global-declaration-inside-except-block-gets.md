# Python 3.13.0 alpha 2 / core and builtins / fix defect where global declaration inside except block gets

[gh-111123](https://github.com/python/cpython/issues/111123): Fix a defect where a [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) declaration inside an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) block gets rejected when the global appears in the [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) block.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
