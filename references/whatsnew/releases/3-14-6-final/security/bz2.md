# Python 3.14.6 final / security / bz2

[gh-150599](https://github.com/python/cpython/issues/150599): Repair a possible stack buffer overflow within [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) once a [`bz2.BZ2Decompressor`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2Decompressor) gets reused following a decompression fault. From now on the decompressor turns unusable once libbz2 signals an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
