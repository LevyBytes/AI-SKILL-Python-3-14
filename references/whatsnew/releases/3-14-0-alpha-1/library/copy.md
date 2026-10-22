# Python 3.14.0 alpha 1 / library / copy

[gh-114264](https://github.com/python/cpython/issues/114264): A fast path for atomic types now makes [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) perform better.

[gh-121141](https://github.com/python/cpython/issues/121141): Extend [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) support to AST nodes. Patch by Bénédikt Tran.

[gh-120108](https://github.com/python/cpython/issues/120108): Repair [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) when it runs over [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) trees that were altered to carry references back to parent nodes. Jelle Zijlstra authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
