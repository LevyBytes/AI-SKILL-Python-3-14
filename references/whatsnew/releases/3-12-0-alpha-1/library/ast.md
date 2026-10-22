# Python 3.12.0 alpha 1 / library / ast

[gh-92986](https://github.com/python/cpython/issues/92986): Repair [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) for the case where `ImportFrom.level` equals `None`

[gh-92671](https://github.com/python/cpython/issues/92671): Patched [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) for empty tuples appearing in the assignment-target context.

[gh-94949](https://github.com/python/cpython/issues/94949): When `feature_version` below `(3, 9)` is supplied, [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) stops parsing parenthesized context managers. Shantanu Jain wrote the patch.

[gh-94947](https://github.com/python/cpython/issues/94947): When `feature_version` below `(3, 8)` is supplied, [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) stops parsing assignment expressions. Shantanu Jain wrote the patch.

[gh-95066](https://github.com/python/cpython/issues/95066): An assert inside [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) is swapped for an exception whenever `feature_version` supplies an invalid major version. Shantanu Jain wrote the patch.

[gh-94996](https://github.com/python/cpython/issues/94996): [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) will from now on decline to parse function definitions carrying positional-only params when handed a `feature_version` under `(3, 8)`. Shantanu Jain wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
