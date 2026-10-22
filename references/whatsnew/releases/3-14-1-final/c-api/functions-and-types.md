# Python 3.14.1 final / c api / functions and types

[gh-140042](https://github.com/python/cpython/issues/140042): Dropped the sqlite3_shutdown call, which risked closing sqlite connections whenever it ran alongside multiple sub interpreters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
