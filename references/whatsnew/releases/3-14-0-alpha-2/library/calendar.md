# Python 3.14.0 alpha 2 / library / calendar

[gh-126476](https://github.com/python/cpython/issues/126476): For [`calendar.month()`](https://docs.python.org/3.14/library/calendar.html#calendar.month) given an incorrect month, raise [`calendar.IllegalMonthError`](https://docs.python.org/3.14/library/calendar.html#calendar.IllegalMonthError), which now subclasses [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
