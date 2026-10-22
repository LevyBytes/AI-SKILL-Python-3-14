# Python 3.14.0 beta 1 / core and builtins / compiler and parser

[gh-126835](https://github.com/python/cpython/issues/126835): Constant folding is moved into the peephole optimizer. The files involved in AST optimization are renamed (Python/ast_opt.c -> Python/ast_preprocess.c), as are the structs (_PyASTOptimizeState -> _PyASTPreprocessState) and the functions (_PyAST_Optimize -> _PyAST_Preprocess, _PyCompile_AstOptimize -> _PyCompile_AstPreprocess).

[gh-131507](https://github.com/python/cpython/issues/131507): Syntax highlighting is now supported by PyREPL. ??ukasz Langa contributed this.

[gh-132479](https://github.com/python/cpython/issues/132479): A compiler crash is fixed that arose in some cases when several module-level annotations contained comprehensions and other nested scopes.

[gh-132449](https://github.com/python/cpython/issues/132449): When a syntax error resembles a misspelled Python keyword, a helpful fix suggestion for the typo is now offered. Pablo Galindo Salgado contributed this.

[gh-131798](https://github.com/python/cpython/issues/131798): The JIT compiler can now strip some type checks from operations over lists, tuples, dictionaries, and sets.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
