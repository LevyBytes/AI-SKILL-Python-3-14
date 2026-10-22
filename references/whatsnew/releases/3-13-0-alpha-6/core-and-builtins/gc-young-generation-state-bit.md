# Python 3.13.0 alpha 6 / core and builtins / switch old space bit young generation objects away toward gcstate

[gh-117108](https://github.com/python/cpython/issues/117108): Switch the old space bit on young-generation objects away from 0 toward gcstate->visited, ensuring any object built during GC carries the right old bit should it migrate into the old generation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
