# Python 3.13.0 alpha 6 / windows / time

[gh-88494](https://github.com/python/cpython/issues/88494): Under Windows, [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) now relies on the `QueryPerformanceCounter()` clock for a resolution finer than 1 us, rather than the `GetTickCount64()` clock whose resolution sits at 15.6 ms. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
