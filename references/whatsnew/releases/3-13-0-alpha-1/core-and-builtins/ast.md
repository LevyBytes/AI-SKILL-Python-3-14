# Python 3.13.0 alpha 1 / core and builtins / ast

[gh-104799](https://github.com/python/cpython/issues/104799): When omitted, [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) node attributes that are lists henceforth default to an empty list. As a result, some code that formerly raised [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) once the AST node was used will instead carry on with the empty list. Jelle Zijlstra prepared the patch.

[gh-107015](https://github.com/python/cpython/issues/107015): The ASYNC and AWAIT tokens are dropped from the Grammar, eliminating any chance of turning `async` and `await` into soft keywords when `feature_version<7` is supplied to [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse).

[gh-109341](https://github.com/python/cpython/issues/109341): A crash while compiling a malformed AST that contains a [`ast.TypeAlias`](https://docs.python.org/3.14/library/ast.html#ast.TypeAlias) is now fixed.

[gh-106396](https://github.com/python/cpython/issues/106396): Whenever an f-string expression carries an empty format specification, the parser now emits an empty [`ast.JoinedStr`](https://docs.python.org/3.14/library/ast.html#ast.JoinedStr) node for it rather than a single-element `ast.JoinedStr` containing an empty-string [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant).

[gh-106145](https://github.com/python/cpython/issues/106145): Make `end_lineno` along with `end_col_offset` mandatory on `type_param` ast nodes.

[gh-105588](https://github.com/python/cpython/issues/105588): Address a situation that might crash while compiling malformed [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) nodes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
