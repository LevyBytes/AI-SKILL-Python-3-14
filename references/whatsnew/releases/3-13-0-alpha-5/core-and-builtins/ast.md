# Python 3.13.0 alpha 5 / core and builtins / ast

[gh-105858](https://github.com/python/cpython/issues/105858): Make the constructors for [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) nodes better. List-typed arguments now fall back to an empty list when left out, and optional fields fall back to `None`. AST nodes now carry an `__annotations__` attribute holding the expected types of their attributes. Handing unrecognized extra arguments to AST nodes is deprecated and turns into an error come Python 3.15. Leaving out a required argument to an AST node is deprecated and turns into an error come Python 3.15. Patch by Jelle Zijlstra.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
