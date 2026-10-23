# What’s New In Python 3.12 / sqlite3 - sqlite3

### sqlite3

- Add a [command-line interface](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-cli). (Contributed by Erlend E. Aasland in [gh-77617](https://github.com/python/cpython/issues/77617).)

- Add the [`sqlite3.Connection.autocommit`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.autocommit) attribute onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) plus the *autocommit* parameter on [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) to drive [**PEP 249**](https://peps.python.org/pep-0249/)-compliant [transaction handling](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-transaction-control-autocommit). (Contributed by Erlend E. Aasland in [gh-83638](https://github.com/python/cpython/issues/83638).)

- Add an *entrypoint* keyword-only parameter onto [`sqlite3.Connection.load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.load_extension) so the entry point of a SQLite extension can be overridden. (Contributed by Erlend E. Aasland in [gh-103015](https://github.com/python/cpython/issues/103015).)

- Add [`sqlite3.Connection.getconfig()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.getconfig) plus [`sqlite3.Connection.setconfig()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.setconfig) onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) for applying configuration tweaks to a database connection. (Contributed by Erlend E. Aasland in [gh-103489](https://github.com/python/cpython/issues/103489).)

### sqlite3

- These undocumented [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) features, deprecated back in Python 3.10, are now gone:

  - `sqlite3.enable_shared_cache()`

  - `sqlite3.OptimizedUnicode`

Where a shared cache is needed, open the database under URI mode and pass the `cache=shared` query parameter.

Ever since Python 3.3, the `sqlite3.OptimizedUnicode` text factory has merely aliased [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). Code that formerly assigned `OptimizedUnicode` as its text factory may either name `str` directly or fall back on the default, which is `str` as well.

(Contributed by Erlend E. Aasland in [gh-92548](https://github.com/python/cpython/issues/92548).)

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](statistics.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](smtpd.md) · [Next source section](ssl.md)
