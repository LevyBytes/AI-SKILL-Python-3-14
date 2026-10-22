# Python 3.13.0 alpha 4 / core and builtins / threading

[gh-114083](https://github.com/python/cpython/issues/114083): The compiler now folds LOAD_CONST together with the instruction that follows it in a distinct pass run ahead of the other optimisations, which permits jump threading under certain conditions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
