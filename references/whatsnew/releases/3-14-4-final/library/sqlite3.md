# Python 3.14.4 final / library / sqlite3

[gh-146090](https://github.com/python/cpython/issues/146090): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3): corrects a crash whenever [`sqlite3.Connection.create_collation()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_collation) fails with [SQLITE_BUSY](https://sqlite.org/rescode.html#busy). Bénédikt Tran supplied the patch.

[gh-146090](https://github.com/python/cpython/issues/146090): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3): now raises [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) correctly in place of [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) whenever a context callback cannot be allocated. Bénédikt Tran supplied the patch.

[gh-142787](https://github.com/python/cpython/issues/142787): An assertion failure in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) blob subscripting, triggered by slice indices that yield an empty slice, has been addressed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
