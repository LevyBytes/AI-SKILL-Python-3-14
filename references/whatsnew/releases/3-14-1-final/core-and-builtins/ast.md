# Python 3.14.1 final / core and builtins / ast

[gh-139640](https://github.com/python/cpython/issues/139640): [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) has stopped issuing syntax warnings over `return`/`break`/`continue` placed in `finally` (refer to [**PEP 765**](https://peps.python.org/pep-0765/)) – such warnings now surface only at compilation time.

[gh-140471](https://github.com/python/cpython/issues/140471): Resolve a possible buffer overflow during [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) node initialization whenever malformed [`_fields`](https://docs.python.org/3.14/library/ast.html#ast.AST._fields) carrying non-[`str`](https://docs.python.org/3.14/library/stdtypes.html#str) entries are met.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
