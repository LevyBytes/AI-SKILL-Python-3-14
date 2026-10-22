# Python 3.9.0 alpha 2 / library / ast

[bpo-38870](https://bugs.python.org/issue?@action=redirect&bpo=38870): Surface [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) as a function of the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module; it can unparse an [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) object and return a string of code that, once parsed, yields an equivalent `ast.AST` object. The patch came jointly from Pablo Galindo and Batuhan Taskaya.

[bpo-38348](https://bugs.python.org/issue?@action=redirect&bpo=38348): Give the ast parsing tool new command line options: `-i` and `--indent` (indentation level), plus `--no-type-comments` (type comments).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
