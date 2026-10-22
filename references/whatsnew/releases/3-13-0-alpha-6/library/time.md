# Python 3.13.0 alpha 6 / library / time

[gh-63207](https://github.com/python/cpython/issues/63207): Under Windows, [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) now draws on the `GetSystemTimePreciseAsFileTime()` clock for resolution finer than 1 us, in place of the `GetSystemTimeAsFileTime()` clock whose resolution sits at 15.6 ms. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
