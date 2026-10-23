# What's New In Python 3.13 / sqlite3 - sqlite3

### sqlite3

- Failing to [`closed`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.close) a [`Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) object explicitly now raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning). (Contributed by Erlend E. Aasland in [gh-105539](https://github.com/python/cpython/issues/105539).)

- A new *filter* keyword-only parameter on [`Connection.iterdump()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.iterdump) lets you select which database objects get dumped. (Contributed by Mariusz Felisiak in [gh-91602](https://github.com/python/cpython/issues/91602).)

[Subject index](INDEX.md) · [Previous source section](site.md) · [Next source section](ssl.md) · [Release/subject declaration](summary-release-highlights.md)
