# Python 3.13.0 alpha 2 / library / drop posix fallocate wasi since backing posix fallocate does not exist

[gh-111804](https://github.com/python/cpython/issues/111804): Drop posix.fallocate() on WASI, since the backing posix_fallocate() does not exist in WASI preview2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
