# Python 3.13.0 alpha 3 / core and builtins / debug

[gh-113603](https://github.com/python/cpython/issues/113603): Fixed a defect in which a redundant NOP went unremoved, triggering a failed assertion inside the compiler under debug mode.

[gh-112215](https://github.com/python/cpython/issues/112215): Tripled the C recursion limit for non-debug builds, leaving webassembly and s390 platforms as they were. Doing so eases certain 3.12 regressions involving deep recursion that interleaves builtin (C) and Python code.

[gh-113054](https://github.com/python/cpython/issues/113054): Fixed a defect in which a redundant NOP went unremoved, triggering a failed assertion inside the compiler under debug mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
