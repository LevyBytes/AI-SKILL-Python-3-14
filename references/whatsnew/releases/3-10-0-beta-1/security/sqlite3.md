# Python 3.10.0 beta 1 / security / sqlite3

[bpo-43434](https://bugs.python.org/issue?@action=redirect&bpo=43434): Building [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) objects now emits `sqlite3.connect` together with `sqlite3.connect/handle` [auditing events](https://docs.python.org/3.14/library/sys.html#auditing) as well. Formerly only [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) calls raised those events. Erlend E. Aasland provided the patch.

[bpo-43762](https://bugs.python.org/issue?@action=redirect&bpo=43762): Introduce audit events covering `sqlite3.connect/handle()`, [`sqlite3.Connection.enable_load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.enable_load_extension), plus [`sqlite3.Connection.load_extension()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.load_extension). Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
