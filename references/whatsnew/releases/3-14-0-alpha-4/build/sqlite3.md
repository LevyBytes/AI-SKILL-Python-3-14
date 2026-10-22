# Python 3.14.0 alpha 4 / build / sqlite3

[gh-128321](https://github.com/python/cpython/issues/128321): While probing whether [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) library functions exist, assign `LIBS` rather than `LDFLAGS`. Doing so corrects the order in which libraries get linked during those probes, which previously went wrong with a statically linked `libsqlite3`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
