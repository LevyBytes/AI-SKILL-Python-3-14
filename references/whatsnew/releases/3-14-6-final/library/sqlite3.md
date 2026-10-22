# Python 3.14.6 final / library / sqlite3

[gh-150913](https://github.com/python/cpython/issues/150913): Adjust [`sqlite3.Blob`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Blob) slice assignment so it throws [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) for type and size mismatches respectively, even where the target slice is empty.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
