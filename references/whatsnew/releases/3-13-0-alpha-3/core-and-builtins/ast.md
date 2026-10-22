# Python 3.13.0 alpha 3 / core and builtins / ast

[gh-106905](https://github.com/python/cpython/issues/106905): Track recursion depth inside the AST parser through per AST-parser state rather than global state, heading off a possible race condition arising from concurrent parsing.

The problem mostly surfaced under 3.11 among multithreaded callers of [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse). Within 3.12 a revision to the timing of garbage collection stopped the race condition from happening.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
