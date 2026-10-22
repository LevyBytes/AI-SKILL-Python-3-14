# Python 3.5.0 alpha 1 / library / sqlite3

[bpo-21858](https://bugs.python.org/issue?@action=redirect&bpo=21858): Python exceptions are now handled more gracefully by the sqlite3 module.

[bpo-21147](https://bugs.python.org/issue?@action=redirect&bpo=21147): Rather than truncating it, sqlite3 now raises an exception when the request holds a null character. Victor Stinner wrote the patch this builds on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
