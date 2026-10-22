# Python 3.13.0 alpha 4 / macos / build and platforms

[gh-115009](https://github.com/python/cpython/issues/115009): Bump the macOS installer to use SQLite 3.45.1.

[gh-109991](https://github.com/python/cpython/issues/109991): Bump the macOS installer to use OpenSSL 3.0.13.

[gh-87804](https://github.com/python/cpython/issues/87804): Under macOS the outcome of `os.statvfs` and `os.fstatvfs` now reports the size of very large disks accurately; in earlier releases the reported block count came out wrong for disks holding 2**32 blocks or more.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
