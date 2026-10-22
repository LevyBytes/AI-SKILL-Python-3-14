# What's New In Python 3.7 / sqlite3 — sqlite3

### sqlite3

[`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) now offers a [`backup()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.backup) method whenever the SQLite library underneath is version 3.6.11 or newer. (Contributed by Lele Gaifax in [bpo-27645](https://bugs.python.org/issue?@action=redirect&bpo=27645).)

For [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect), the *database* argument will now take any [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) and not merely a string. (Contributed by Anders Lorentsen in [bpo-31843](https://bugs.python.org/issue?@action=redirect&bpo=31843).)

[Subject index](INDEX.md) · [Previous source section](socketserver.md) · [Next source section](ssl.md) · [Release/subject declaration](summary-release-highlights.md)
