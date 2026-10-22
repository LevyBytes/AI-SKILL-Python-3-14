# Python 3.11.0 alpha 1 / core and builtins / ast

[bpo-44885](https://bugs.python.org/issue?@action=redirect&bpo=44885): Fixed the ast locations for f-strings that carry format specs along with repeated expressions. Pablo Galindo wrote the fix.

[bpo-11105](https://bugs.python.org/issue?@action=redirect&bpo=11105): While compiling [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) objects that hold recursive references via [`compile()`](https://docs.python.org/3.14/library/functions.html#compile), the interpreter no longer crashes; it now raises a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
