# Python 3.13.0 alpha 1 / core and builtins / tp dealloc defined counteroptimizer type removes segfault deallocation

[gh-108727](https://github.com/python/cpython/issues/108727): A `tp_dealloc` was defined for `CounterOptimizer_Type`, which removes a segfault on deallocation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
