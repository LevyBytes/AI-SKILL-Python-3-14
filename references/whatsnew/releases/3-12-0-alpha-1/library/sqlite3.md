# Python 3.12.0 alpha 1 / library / sqlite3

[gh-95132](https://github.com/python/cpython/issues/95132): A [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) regression is fixed wherein `*args` and `**kwds` were wrongly forwarded from [`connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) on to the [`Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) factory. This regression first appeared in 3.11a1 via PR 24421 ([gh-85128](https://github.com/python/cpython/issues/85128)). Erlend E. Aasland wrote the patch.

[gh-93044](https://github.com/python/cpython/issues/93044): Stop coercing the database argument given to [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) into bytes before it reaches the factory.

[gh-90016](https://github.com/python/cpython/issues/90016): The [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) [default adapters and converters](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-default-converters) are deprecated. Erlend E. Aasland wrote the patch.

[gh-79579](https://github.com/python/cpython/issues/79579): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) now reliably recognizes DML queries that begin with comments. Erlend E. Aasland supplied the patch.

[gh-93421](https://github.com/python/cpython/issues/93421): Refresh [`sqlite3.Cursor.rowcount`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.rowcount) once a DML statement has finished executing. This corrects the row tally for SQL such as `UPDATE ... RETURNING`. Erlend E. Aasland supplied the patch.

[gh-92547](https://github.com/python/cpython/issues/92547): Drop undocumented [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) features that were deprecated as of Python 3.10:

  - `sqlite3.enable_shared_cache()`

  - `sqlite3.OptimizedUnicode`

Erlend E. Aasland supplied the patch.

[gh-77617](https://github.com/python/cpython/issues/77617): A [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) [command-line interface](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-cli) is added. Erlend Aasland wrote the patch.

[bpo-34828](https://bugs.python.org/issue?@action=redirect&bpo=34828): Databases relying on `AUTOINCREMENT` across one or more tables are now handled correctly by [`sqlite3.Connection.iterdump()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.iterdump).

[gh-94028](https://github.com/python/cpython/issues/94028): Correct a [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) regression where statement objects went uncleared and unreset once a cursor had iterated over them. PR 27884 had introduced this in Python 3.11a1. Erlend E. Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
