# Python 3.13.0 alpha 4 / library / dbm

[gh-100414](https://github.com/python/cpython/issues/100414): Bring in [`dbm.sqlite3`](https://docs.python.org/3.14/library/dbm.html#module-dbm.sqlite3) as one more backend for [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm), and elevate it to the new default `dbm` backend. Raymond Hettinger and Erlend E. Aasland wrote the patch.

[gh-83383](https://github.com/python/cpython/issues/83383): Syncing the [`dbm.dumb`](https://docs.python.org/3.14/library/dbm.html#module-dbm.dumb) database now becomes a no-op when nothing changed since the open or the most recent sync. For a freshly built empty `dbm.dumb` database, the directory file gets written right after opening rather than postponing that work until a sync or a close.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
