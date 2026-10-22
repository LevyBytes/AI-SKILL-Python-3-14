# Python 3.12.0 alpha 1 / documentation / ast

[gh-95588](https://github.com/python/cpython/issues/95588): Resolved the contradictory guidance in the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) docs, which described [`ast.literal_eval()`](https://docs.python.org/3.14/library/ast.html#ast.literal_eval) as "safe" against untrusted input yet simultaneously cautioned that it could crash the process. That second claim holds and is considered unfixable short of a large effort inappropriate for a bugfix. We therefore retain the caution and stop asserting that `literal_eval` is safe.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
