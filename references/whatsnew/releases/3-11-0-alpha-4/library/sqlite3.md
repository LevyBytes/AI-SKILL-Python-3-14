# Python 3.11.0 alpha 4 / library / sqlite3

[bpo-44092](https://bugs.python.org/issue?@action=redirect&bpo=44092): A fetch performed across a rollback no longer raises [`InterfaceError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.InterfaceError); instead these situations are left for the SQLite library to manage. Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
