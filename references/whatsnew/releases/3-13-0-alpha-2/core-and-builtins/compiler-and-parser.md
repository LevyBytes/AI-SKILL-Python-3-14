# Python 3.13.0 alpha 2 / core and builtins / compiler and parser

[gh-111654](https://github.com/python/cpython/issues/111654): Fix the runtime crash arising when something goes wrong in the `LOAD_FROM_DICT_OR_DEREF` opcode.

[gh-111520](https://github.com/python/cpython/issues/111520): Fuse the Tier 1 (bytecode) and Tier 2 (micro-ops) interpreters, relocating the Tier 2 loop and switch into `_PyEval_EvalFrameDefault()` over in `Python/ceval.c`. The `Python/executor.c` file no longer exists. The code generator now also handles the `TIER_ONE` and `TIER_TWO` macros.

**Beware!** With this, the environment variables that enable micro-ops and their debugging become `PYTHON_UOPS` and `PYTHON_LLTRACE`.

[gh-110864](https://github.com/python/cpython/issues/110864): Repair `_PyArg_UnpackKeywordsWithVararg` argument parsing for functions that declare pos-or-keyword, vararg, and kw-only parameters.

[gh-106905](https://github.com/python/cpython/issues/106905): Repair the bogus SystemError about an AST constructor recursion depth mismatch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
