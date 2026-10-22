# Python 3.12.0 beta 1 / library / sqlite3

[gh-102628](https://github.com/python/cpython/issues/102628): On Windows, swap CTRL-D for CTRL-Z inside the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) CLI banner.

[gh-103015](https://github.com/python/cpython/issues/103015): Provide an *entrypoint* keyword-only parameter on [`sqlite3.Connection.load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.load_extension) for overriding which SQLite extension entry point is used. Erlend E. Aasland authored the patch.

[gh-103489](https://github.com/python/cpython/issues/103489): Provide [`getconfig()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.getconfig) plus [`setconfig()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.setconfig) on [`Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) so configuration of a database connection can be altered. Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
