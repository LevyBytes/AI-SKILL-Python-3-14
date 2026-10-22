# Python 3.14.0 alpha 7 / library / ast

[gh-129598](https://github.com/python/cpython/issues/129598): Corrected [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) for the case where [`ast.Interactive`](https://docs.python.org/3.14/library/ast.html#ast.Interactive) holds several statements.

[gh-118761](https://github.com/python/cpython/issues/118761): Sped up importing the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module by pulling the [`unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) function out into a helper module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
