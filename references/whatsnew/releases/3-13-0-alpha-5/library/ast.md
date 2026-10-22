# Python 3.13.0 alpha 5 / library / ast

[gh-115881](https://github.com/python/cpython/issues/115881): Repair the case where [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) wrongly tagged conditional context managers (for instance `with (x() if y else z()): ...`) as bad syntax when `feature_version=(3, 8)` got passed. This undoes the grammar changes introduced as part of [gh-94949](https://github.com/python/cpython/issues/94949).

[gh-112364](https://github.com/python/cpython/issues/112364): Fixed [`ast.unparse()`](https://docs.python.org/3.14/library/ast.html#ast.unparse) so it deals with a format_spec holding `"`, `'` or `\\`. Patched by Frank Hoffmann.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
