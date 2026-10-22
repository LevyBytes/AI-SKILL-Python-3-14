# Python 3.14.0 alpha 4 / library / tempfile

[gh-126639](https://github.com/python/cpython/issues/126639): [`tempfile.NamedTemporaryFile`](https://docs.python.org/3.14/library/tempfile.html#tempfile.NamedTemporaryFile) is now going to emit a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) whenever the garbage collector finalizes it and it was never closed on purpose.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
