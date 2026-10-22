# Python 3.14.0 alpha 3 / core and builtins / modules

[gh-126491](https://github.com/python/cpython/issues/126491): Give the GC a marking phase. Ahead of cycle detection, everything transitively reachable from the stacks or from builtin modules gets flagged as reachable. The GC consequently performs roughly 50% less work.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
