# Python 3.11.0 alpha 1 / library / ast

[bpo-44142](https://bugs.python.org/issue?@action=redirect&bpo=44142): [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) will from now on remove the unneeded parentheses where tuples serve as assignment targets (such as in for loops).

[bpo-44081](https://bugs.python.org/issue?@action=redirect&bpo=44081): [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) no longer inserts a needless space to set off `lambda` from the `:` when there are no parameters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
