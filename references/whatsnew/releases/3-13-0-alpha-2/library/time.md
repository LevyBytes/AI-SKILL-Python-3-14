# Python 3.13.0 alpha 2 / library / time

[gh-111295](https://github.com/python/cpython/issues/111295): Correct [`time`](https://docs.python.org/3.14/library/time.html#module-time) failing to check for errors during initialization.

[gh-111482](https://github.com/python/cpython/issues/111482): [`time`](https://docs.python.org/3.14/library/time.html#module-time): A faster calling convention now makes [`time.clock_gettime()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime) and [`time.clock_gettime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime_ns) run as much as 2x quicker. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
