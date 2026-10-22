# Python 3.14.0 alpha 1 / core and builtins / builtins

[gh-119213](https://github.com/python/cpython/issues/119213): Modules outside the builtins that were built using argument clinic kept crashing whenever they ran in a subinterpreter prior to the main interpreter. The culprit objects, which leaked carelessly across interpreters, have now been corrected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
