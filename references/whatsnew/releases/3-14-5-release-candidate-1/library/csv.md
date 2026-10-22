# Python 3.14.5 release candidate 1 / library / csv

[gh-145105](https://github.com/python/cpython/issues/145105): Stop a crash in the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) reader that struck while looping with a re-entrant iterator calling [`next()`](https://docs.python.org/3.14/library/functions.html#next) on that very reader from inside `__next__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
