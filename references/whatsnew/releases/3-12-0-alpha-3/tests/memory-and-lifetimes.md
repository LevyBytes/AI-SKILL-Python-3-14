# Python 3.12.0 alpha 3 / tests / memory and lifetimes

[gh-99659](https://github.com/python/cpython/issues/99659): The optional big memory tests within `test_sqlite3` now trap the right `sqlite.DataError` exception type whenever oversized strings and/or blobs are passed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
