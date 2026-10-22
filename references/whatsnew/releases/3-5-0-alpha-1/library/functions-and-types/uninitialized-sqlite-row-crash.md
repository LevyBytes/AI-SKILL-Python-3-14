# Python 3.5.0 alpha 1 / library / crash touching uninitialized sqlite3 row fixed notably unpickling pickled sqlite3 row

[bpo-21975](https://bugs.python.org/issue?@action=redirect&bpo=21975): A crash from touching an uninitialized sqlite3.Row was fixed (notably when unpickling a pickled sqlite3.Row). The __new__() method now performs the initialization of sqlite3.Row.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
