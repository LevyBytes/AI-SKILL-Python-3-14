# Python 3.14.3 final / library / inspect

[gh-143999](https://github.com/python/cpython/issues/143999): An issue where [`inspect.getgeneratorstate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getgeneratorstate) and [`inspect.getcoroutinestate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcoroutinestate) might break for generators in the suspended state that had been wrapped by [`types.coroutine()`](https://docs.python.org/3.14/library/types.html#types.coroutine) is now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
