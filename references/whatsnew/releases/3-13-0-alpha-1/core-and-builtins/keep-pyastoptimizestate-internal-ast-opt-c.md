# Python 3.13.0 alpha 1 / core and builtins / keep pyastoptimizestate internal ast opt c

[gh-105148](https://github.com/python/cpython/issues/105148): Keep `_PyASTOptimizeState` internal to ast_opt.c. Have `_PyAST_Optimize` accept a pair of integers rather than a pointer to that struct. This removes any need to pull pycore_compile.h into ast_opt.c.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
