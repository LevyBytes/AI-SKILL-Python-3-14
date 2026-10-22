# Python 3.14.0 alpha 1 / library / gzip

[gh-125260](https://github.com/python/cpython/issues/125260): For reproducible output, the [`gzip.compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) *mtime* parameter now defaults to 0. Patch by Bernhard M. Wiedemann and Adam Turner.

[gh-90425](https://github.com/python/cpython/issues/90425): When [`gzip.compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) is called, the OS byte within gzip headers is henceforth fixed at 255.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
