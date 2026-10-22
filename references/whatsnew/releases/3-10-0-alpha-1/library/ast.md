# Python 3.10.0 alpha 1 / library / ast

[bpo-41887](https://bugs.python.org/issue?@action=redirect&bpo=41887): [`ast.literal_eval()`](https://docs.python.org/3.14/library/ast.html#ast.literal_eval) now strips leading spaces and tabs. The stripping of spaces and tabs for [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) is now documented too.

[bpo-40726](https://bugs.python.org/issue?@action=redirect&bpo=40726): Cope with situations where `end_lineno` is `None` during [`ast.increment_lineno()`](https://docs.python.org/3.14/library/ast.html#ast.increment_lineno).

[bpo-40614](https://bugs.python.org/issue?@action=redirect&bpo=40614): [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) declines to parse self-documenting f-string expressions whenever the `feature_version` it receives is below `(3, 8)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
