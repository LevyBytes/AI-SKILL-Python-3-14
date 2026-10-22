# Python 3.14.0 beta 2 / library / ast

[gh-133581](https://github.com/python/cpython/issues/133581): Better unparsing of t-strings through [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) and `from __future__ import annotations`. Empty t-strings now round-trip properly and formatting inside interpolations is kept. Patch by Jelle Zijlstra.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
