# Python 3.14.0 release candidate 2 / core and builtins / exceptions

[gh-137308](https://github.com/python/cpython/issues/137308): When a node body holds a lone docstring, it is now compiled down to a [`pass`](https://docs.python.org/3.14/reference/simple_stmts.html#pass) statement so the body of that node is never left empty. Without this, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) surfaced from [`compile()`](https://docs.python.org/3.14/library/functions.html#compile).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
