# Python 3.14.0 alpha 7 / library / gzip

[gh-131492](https://github.com/python/cpython/issues/131492): Plugged a resource leak that occurred when building a [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) with a filename fails — for instance, after passing an invalid `compresslevel`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
