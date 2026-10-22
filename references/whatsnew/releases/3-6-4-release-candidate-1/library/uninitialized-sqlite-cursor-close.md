# Python 3.6.4 release candidate 1 / library / stop crash inside sqlite3 cursor close whenever cursor object not initialized

[bpo-31764](https://bugs.python.org/issue?@action=redirect&bpo=31764): Stop a crash inside `sqlite3.Cursor.close()` whenever the `Cursor` object has not been initialized. Oren Milman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
