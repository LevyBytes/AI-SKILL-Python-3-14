# Python 3.11.0 beta 1 / core and builtins / decimal

[gh-91428](https://github.com/python/cpython/issues/91428): For debug builds, add `static const char *const _PyOpcode_OpName[256] = {...};` into `opcode.h` to help with debugging the Python interpreter. Producing more human-readable debugging output is now easier because opcode names can be shown rather than only their matching decimal digits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
