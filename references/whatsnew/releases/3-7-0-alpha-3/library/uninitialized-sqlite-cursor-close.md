# Python 3.7.0 alpha 3 / library / avoid crash inside sqlite3 cursor close whenever cursor object not initialized

[bpo-31764](https://bugs.python.org/issue?@action=redirect&bpo=31764): Avoid a crash inside `sqlite3.Cursor.close()` whenever the `Cursor` object has not been initialized. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
