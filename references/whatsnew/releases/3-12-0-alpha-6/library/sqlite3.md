# Python 3.12.0 alpha 6 / library / sqlite3

[gh-101693](https://github.com/python/cpython/issues/101693): Inside [`sqlite3.Cursor.execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute), a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) now fires whenever [named placeholders](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-placeholders) appear alongside parameters handed over as a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) rather than as a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). As of Python 3.14, pairing named placeholders with parameters given as a sequence will throw a [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). Erlend E. Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
