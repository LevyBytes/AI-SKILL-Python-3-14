# Python 3.12.0 alpha 1 / c api / compiler and parser

[gh-92781](https://github.com/python/cpython/issues/92781): Keep declarations and code separate throughout the C API so the "ISO C90 forbids mixed declarations and code" [-Werror=declaration-after-statement] compiler warning goes away. Victor Stinner provided the patch.

[gh-59121](https://github.com/python/cpython/issues/59121): Repaired an assert that had blocked `PyRun_InteractiveOne` from yielding tracebacks while parsing from the supplied FD.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
