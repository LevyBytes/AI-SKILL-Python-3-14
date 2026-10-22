# Python 3.14.1 final / library / dbm

[gh-127081](https://github.com/python/cpython/issues/127081): Resolve libc thread safety problems affecting [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm) by running its stateful operations within critical sections.

[gh-140272](https://github.com/python/cpython/issues/140272): A memory leak in the `clear()` method belonging to the [`dbm.gnu`](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu) database is fixed.

[gh-135386](https://github.com/python/cpython/issues/135386): Correct read access to a [`dbm.sqlite3`](https://docs.python.org/3.14/library/dbm.html#module-dbm.sqlite3) database backed by a read-only file or directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
