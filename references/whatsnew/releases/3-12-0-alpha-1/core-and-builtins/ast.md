# Python 3.12.0 alpha 1 / core and builtins / ast

[gh-93351](https://github.com/python/cpython/issues/93351): [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) node positions now undergo validation when supplied to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) and other related functions. Should invalid positions be spotted, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

[gh-93359](https://github.com/python/cpython/issues/93359): Guarantees custom [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) nodes lacking explicit end positions still compile. Pablo Galindo wrote the patch.

[gh-94869](https://github.com/python/cpython/issues/94869): Corrects the column offsets for certain expressions inside multi-line f-strings within [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) nodes. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
