# Python 3.8.0 alpha 1 / library / sqlite3

[bpo-34041](https://bugs.python.org/issue?@action=redirect&bpo=34041): The [`sqlite3.Connection.create_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_function) method gains a *deterministic* parameter. Patch by Sergey Fedoseev.

[bpo-27645](https://bugs.python.org/issue?@action=redirect&bpo=27645): [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) now offers a [`backup`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.backup) method whenever the SQLite library underneath is version 3.6.11 or newer. Patch by Lele Gaifax.

[bpo-32215](https://bugs.python.org/issue?@action=redirect&bpo=32215): Corrected a speed regression in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) that struck whenever a DML statement sat on a separate line from the remaining SQL query text.

[bpo-34052](https://bugs.python.org/issue?@action=redirect&bpo=34052): The [`sqlite3.Connection.create_aggregate()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_aggregate), [`sqlite3.Connection.create_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_function), [`sqlite3.Connection.set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer), [`sqlite3.Connection.set_progress_handler()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_progress_handler) methods now raise TypeError whenever unhashable objects arrive as the callable. Such objects are no longer forwarded to the SQLite API by these methods. The earlier behavior risked segfaults. Patch by Sergey Fedoseev.

[bpo-32788](https://bugs.python.org/issue?@action=redirect&bpo=32788): Within the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module, exceptions besides [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) thrown inside the `__adapt__()` and `__conform__()` methods are now surfaced to the user.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
