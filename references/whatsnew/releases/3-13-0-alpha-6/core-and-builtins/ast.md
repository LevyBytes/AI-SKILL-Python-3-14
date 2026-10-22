# Python 3.13.0 alpha 6 / core and builtins / ast

[gh-117266](https://github.com/python/cpython/issues/117266): Stop crashes affecting certain user-defined subclasses of [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST). Such subclasses are now required to define the `_field_types` attribute.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
