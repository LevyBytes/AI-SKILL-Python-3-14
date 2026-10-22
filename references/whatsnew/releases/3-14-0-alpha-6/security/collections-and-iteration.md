# Python 3.14.0 alpha 6 / security / collections and iteration

[gh-127371](https://github.com/python/cpython/issues/127371): Prevents `tempfile.SpooledTemporaryFile.writelines()` from buffering without bound. Formerly, the spillover to disk got checked only once the lines iterator ran dry. That check now happens after every single line is written.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
