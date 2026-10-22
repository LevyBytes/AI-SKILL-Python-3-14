# Python 3.14.0 alpha 1 / library / profile

[gh-120289](https://github.com/python/cpython/issues/120289): Resolve the use-after-free in [`cProfile`](https://docs.python.org/3.14/library/profile.html#module-cProfile) by forbidding `disable()` together with `clear()` inside external timers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
