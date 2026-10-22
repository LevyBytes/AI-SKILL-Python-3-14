# What's New In Python 3.2 / sqlite3 — sqlite3

### sqlite3

Tracking pysqlite version 2.6.0, the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module picked up two new abilities.

- When uncommitted changes belong to an open transaction, the `sqlite3.Connection.in_transit` attribute reports true.

- Through the [`sqlite3.Connection.enable_load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.enable_load_extension) and [`sqlite3.Connection.load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.load_extension) methods you can pull in SQLite extensions out of “.so” files. A familiar example is the fulltext-search extension that ships alongside SQLite.

(Contributed by R. David Murray and Shashwat Anand; [bpo-8845](https://bugs.python.org/issue?@action=redirect&bpo=8845).)

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](html.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
