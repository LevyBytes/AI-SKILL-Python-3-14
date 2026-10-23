# What's new in Python 3.14 / sqlite3 - sqlite3

### sqlite3

- `version` plus `version_info` no longer live on the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module; reach for [`sqlite_version`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.sqlite_version) and [`sqlite_version_info`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.sqlite_version_info) when you want the true version of the SQLite library at runtime. (Contributed by Hugo van Kemenade in [gh-118924](https://github.com/python/cpython/issues/118924).)

- Combining a parameter sequence together with named placeholders now triggers a [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError); that combination had been deprecated as of Python 3.12. (Contributed by Erlend E. Aasland in [gh-118928](https://github.com/python/cpython/issues/118928) and [gh-101693](https://github.com/python/cpython/issues/101693).)

[Subject index](INDEX.md) · [Previous source section](pty.md) · [Next source section](urllib.md) · [Release/subject declaration](summary-release-highlights.md)
