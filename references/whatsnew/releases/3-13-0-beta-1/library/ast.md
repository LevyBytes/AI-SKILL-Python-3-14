# Python 3.13.0 beta 1 / library / ast

[gh-116023](https://github.com/python/cpython/issues/116023): By default, [`ast.dump()`](https://docs.python.org/3.14/library/ast.html#ast.dump) no longer prints empty fields (those whose value is `None` or `[]`). A new `show_empty=False` parameter lets you display them if desired.

[gh-117486](https://github.com/python/cpython/issues/117486): Refines how user-defined subclasses of [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) behave. In the common scenario, such subclasses will now need no modifications to remain consistent with the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module behavior changes of Python 3.13. Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
