# Python 3.12.0 alpha 2 / library / sqlite3

[gh-83638](https://github.com/python/cpython/issues/83638): Introduce the [`autocommit`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.autocommit) attribute on [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) plus the *autocommit* parameter on [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) for steering [**PEP 249**](https://peps.python.org/pep-0249/)-compliant [transaction handling](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-transaction-control-autocommit). Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
