# Python 3.14.0 release candidate 2 / core and builtins / compiler and parser

[gh-137288](https://github.com/python/cpython/issues/137288): Repair a defect in which certain bytecode instructions belonging to a boolean expression were tied to the wrong exception handler.

[gh-134291](https://github.com/python/cpython/issues/134291): Drop some of the newer macOS API calls from the JIT compiler so that older OSX 10.15 deployment targets stay compatible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
