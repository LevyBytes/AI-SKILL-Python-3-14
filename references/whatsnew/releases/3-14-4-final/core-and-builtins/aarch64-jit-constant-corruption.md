# Python 3.14.4 final / core and builtins / corrects defect might leave constant values partly corrupted within

[gh-146128](https://github.com/python/cpython/issues/146128): Corrects a defect that might leave constant values partly corrupted within AArch64 JIT code. The problem is purely theoretical and has never surfaced in unmodified Python interpreters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
