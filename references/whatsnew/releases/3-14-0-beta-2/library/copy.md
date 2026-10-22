# Python 3.14.0 beta 2 / library / copy

[gh-133783](https://github.com/python/cpython/issues/133783): Repair the bug that arose when [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) was applied to [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) objects. Attributes defaulting to `None` were wrongly considered required on manually built AST nodes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
