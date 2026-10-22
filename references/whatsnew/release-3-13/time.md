# What's New In Python 3.13 / time — time

### time

- Under Windows, [`monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) switches to the `QueryPerformanceCounter()` clock, giving a 1 microsecond resolution, away from the `GetTickCount64()` clock whose resolution is 15.6 milliseconds. (Contributed by Victor Stinner in [gh-88494](https://github.com/python/cpython/issues/88494).)

- Under Windows, [`time()`](https://docs.python.org/3.14/library/time.html#time.time) switches to the `GetSystemTimePreciseAsFileTime()` clock, giving a 1 microsecond resolution, away from the `GetSystemTimeAsFileTime()` clock whose resolution is 15.6 milliseconds. (Contributed by Victor Stinner in [gh-63207](https://github.com/python/cpython/issues/63207).)

[Subject index](INDEX.md) · [Previous source section](tempfile.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)
