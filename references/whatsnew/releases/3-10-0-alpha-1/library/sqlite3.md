# Python 3.10.0 alpha 1 / library / sqlite3

[bpo-41662](https://bugs.python.org/issue?@action=redirect&bpo=41662): Exceptions thrown from `__len__()` of a sequence of parameters are no longer overridden by [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError) in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3).

[bpo-41638](https://bugs.python.org/issue?@action=redirect&bpo=41638): For a missing parameter, the [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError) message in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) now carries the parameter's name rather than its index whenever parameters arrive as a dict.

[bpo-41662](https://bugs.python.org/issue?@action=redirect&bpo=41662): Resolved a crash that struck when the list of parameters was mutated mid-iteration within [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3).

[bpo-40744](https://bugs.python.org/issue?@action=redirect&bpo=40744): The [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module relies on SQLite API functions that need SQLite v3.7.3 or above. This change drops support for the older SQLite releases and now explicitly requires SQLite 3.7.3 at build, compile, and run time alike. Patch by Sergey Fedoseev and Erlend E. Aasland.

[bpo-40737](https://bugs.python.org/issue?@action=redirect&bpo=40737): Close a possible reference leak tied to [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) initialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
