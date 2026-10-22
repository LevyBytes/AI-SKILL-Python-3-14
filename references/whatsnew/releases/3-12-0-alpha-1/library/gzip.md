# Python 3.12.0 alpha 1 / library / gzip

[gh-94196](https://github.com/python/cpython/issues/94196): [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip): The `filename` attribute on [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile), deprecated all the way back in Python 2.6, has been removed; reach for the [`name`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile.name) attribute instead. When opened for writing, that `filename` attribute used to tack on a `'.gz'` extension whenever one was missing. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
