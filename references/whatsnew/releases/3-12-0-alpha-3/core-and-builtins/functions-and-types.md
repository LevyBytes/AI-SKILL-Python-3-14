# Python 3.12.0 alpha 3 / core and builtins / functions and types

[gh-91053](https://github.com/python/cpython/issues/91053): Optimizing interpreters and JIT compilers sometimes have to invalidate their internal metadata whenever functions change. This work supplies the means to register a callback that runs every time a function gets created, altered, or torn down.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
