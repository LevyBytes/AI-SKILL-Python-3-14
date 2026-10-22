# Python 3.8.0 alpha 1 / library / dbm

[bpo-34248](https://bugs.python.org/issue?@action=redirect&bpo=34248): The filename is now reported in the exception raised whenever the database file cannot be opened by [`dbm.gnu.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.gnu.open) and [`dbm.ndbm.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.ndbm.open) on account of an OS-related error. Zsolt Cserna wrote the patch.

[bpo-32749](https://bugs.python.org/issue?@action=redirect&bpo=32749): Opening a [`dbm.dumb`](https://docs.python.org/3.14/library/dbm.html#module-dbm.dumb) database under flags "r" now yields a read-only handle. Calling [`dbm.dumb.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.dumb.open) under flags "r" as well as "w" will no longer build a database when none is present.

[bpo-33383](https://bugs.python.org/issue?@action=redirect&bpo=33383): Repaired a crash in the get() method on the [`dbm.ndbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) database object that struck when it received a single argument.

[bpo-33106](https://bugs.python.org/issue?@action=redirect&bpo=33106): Removing a key out of a read-only dbm database now raises a module specific error rather than KeyError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
