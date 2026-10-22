# Python 3.8.0 alpha 1 / library / ast

[bpo-32892](https://bugs.python.org/issue?@action=redirect&bpo=32892): All constants are now represented by the parser as [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) in place of the dedicated constant AST types (`Num`, `Str`, `Bytes`, `NameConstant` and `Ellipsis`). Those classes count as deprecated and are slated for removal in a later Python release.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
