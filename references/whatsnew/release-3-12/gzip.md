# What’s New In Python 3.12 / gzip - gzip

### gzip

- Drop the `filename` attribute on the [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) of [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip), deprecated as far back as Python 2.6; use the [`name`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile.name) attribute instead. Under write mode, the `filename` attribute tacked on a `'.gz'` file extension whenever one was missing. (Contributed by Victor Stinner in [gh-94196](https://github.com/python/cpython/issues/94196).)

[Subject index](INDEX.md) · [Previous source section](ftplib.md) · [Next source section](hashlib.md) · [Release/subject declaration](summary-release-highlights.md)
