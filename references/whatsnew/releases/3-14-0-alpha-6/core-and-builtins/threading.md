# Python 3.14.0 alpha 6 / core and builtins / threading

[gh-127705](https://github.com/python/cpython/issues/127705): Tagged references (`_PyStackRef`) are now used for the default build in addition to the free-threading build. The short-term cost is a slight performance dip, yet it opens the door to bigger speedups later and substantially cuts maintenance effort by permitting one tagged-reference implementation down the road.

[gh-129967](https://github.com/python/cpython/issues/129967): On the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build, a race condition that surfaced when `repr(set)` ran at the same time as `set.clear()` has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
