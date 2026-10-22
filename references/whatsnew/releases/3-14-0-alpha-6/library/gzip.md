# Python 3.14.0 alpha 6 / library / gzip

[gh-130806](https://github.com/python/cpython/issues/130806): A [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) deleted prior to being closed now raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

[gh-129726](https://github.com/python/cpython/issues/129726): Stops [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) from throwing an unraisable exception while garbage collection runs against a temporary object, achieved by severing the reference loop using [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
