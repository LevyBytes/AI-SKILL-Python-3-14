# Python 3.11.0 alpha 2 / library / sqlite3

[bpo-42064](https://bugs.python.org/issue?@action=redirect&bpo=42064): Move [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) over to multi-phase initialisation (PEP 489). Erlend E. Aasland supplied the patches.

[bpo-45613](https://bugs.python.org/issue?@action=redirect&bpo=45613): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) now derives [`sqlite3.threadsafety`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.threadsafety) from the default threading mode that the underlying SQLite library was compiled with. Erlend E. Aasland wrote the patch.

[bpo-45581](https://bugs.python.org/issue?@action=redirect&bpo=45581): [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) now properly raises [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) whenever the underlying SQLite API reports a memory error. Erlend E. Aasland wrote the patch.

[bpo-24139](https://bugs.python.org/issue?@action=redirect&bpo=24139): Support SQLite extended result codes through [`sqlite3.Error`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Error). Erlend E. Aasland wrote the patch.

[bpo-45243](https://bugs.python.org/issue?@action=redirect&bpo=45243): Add [`setlimit()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.setlimit) along with [`getlimit()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.getlimit) onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) so SQLite limits can be set and read on a per-connection basis. Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
