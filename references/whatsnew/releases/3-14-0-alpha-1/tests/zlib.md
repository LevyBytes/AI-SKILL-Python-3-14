# Python 3.14.0 alpha 1 / tests / zlib

[gh-125041](https://github.com/python/cpython/issues/125041): Restore the previously skipped [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) tests on the s390x architecture: only the comparison of the compressed bytes is now skipped, since zlib's software path and the hardware-accelerated path may produce differing output.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
