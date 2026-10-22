# Python 3.9.0 alpha 1 / library / sqlite3

[bpo-37406](https://bugs.python.org/issue?@action=redirect&bpo=37406): Should the operation argument fail to be a str, the sqlite3 module now throws TypeError in place of ValueError, covering execute(), executemany() and calling a connection.

[bpo-37347](https://bugs.python.org/issue?@action=redirect&bpo=37347): The [`sqlite3.Connection.create_aggregate()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_aggregate), [`sqlite3.Connection.create_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_function), [`sqlite3.Connection.set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer), [`sqlite3.Connection.set_progress_handler()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_progress_handler) [`sqlite3.Connection.set_trace_callback()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_trace_callback) methods would segfault whenever any of them was invoked a second time with an equal object that was not the same object. Callbacks are now kept with greater care. Aleksandr Balezin contributed the patch.

[bpo-38185](https://bugs.python.org/issue?@action=redirect&bpo=38185): A case-insensitive string comparison during [`sqlite3.Row`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Row) indexing was fixed.

[bpo-38175](https://bugs.python.org/issue?@action=redirect&bpo=38175): A memory leak that occurred while comparing [`sqlite3.Row`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Row) objects was repaired.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
