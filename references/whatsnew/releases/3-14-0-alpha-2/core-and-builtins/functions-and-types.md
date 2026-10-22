# Python 3.14.0 alpha 2 / core and builtins / functions and types

[gh-125868](https://github.com/python/cpython/issues/125868): Exclusively in 3.14.0a1, attribute lookup could return an incorrect value. The culprit was a faulty specialization arising under very narrow conditions. A fix landed in 3.14.0a2.

[gh-125498](https://github.com/python/cpython/issues/125498): Clang 19's newly added `preserve_none` attribute is now exploited by the JIT; it covers more platforms and proves more practical than the `ghccc` calling convention LLVM already offered. As a bonus, hand-patching the calling convention within LLVM IR is no longer required, which streamlines how the JIT compiles.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
