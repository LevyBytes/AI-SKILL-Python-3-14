# Python 3.11.0 beta 1 / library / sqlite3

[gh-89022](https://github.com/python/cpython/issues/89022): For [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3), `SQLITE_MISUSE` result codes now translate to [`InterfaceError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.InterfaceError) rather than [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). On top of that, parameter-binding failures now surface clearer exceptions. Erlend E. Aasland wrote the patch.

[gh-69093](https://github.com/python/cpython/issues/69093): Give [`sqlite3.Blob`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Blob) the ability to be indexed and sliced. Aviv Palivoda and Erlend E. Aasland prepared the patch.

[gh-69093](https://github.com/python/cpython/issues/69093): Let [`sqlite3.Blob`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Blob) act as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager). Aviv Palivoda and Erlend E. Aasland prepared the patch.

[bpo-45138](https://bugs.python.org/issue?@action=redirect&bpo=45138): Repair a regression within the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) trace callback, where bound parameters had stopped being expanded in the statement string that is handed over. That regression first appeared in Python 3.10 because of [bpo-40318](https://bugs.python.org/issue?@action=redirect&bpo=40318). Erlend E. Aasland authored the patch.

[bpo-40617](https://bugs.python.org/issue?@action=redirect&bpo=40617): Equip [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) with [`create_window_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_window_function) so that aggregate window functions can be defined. Erlend E. Aasland authored the patch.

[bpo-36073](https://bugs.python.org/issue?@action=redirect&bpo=36073): Instead of segfaulting on recursive use of cursors in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) converters, raise [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). Sergey Fedoseev authored the patch.

[bpo-24905](https://bugs.python.org/issue?@action=redirect&bpo=24905): Equip [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) with [`blobopen()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.blobopen). [`sqlite3.Blob`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Blob) enables incremental I/O operations on blobs. Aviv Palivoda and Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
