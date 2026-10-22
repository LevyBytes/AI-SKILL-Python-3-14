# Python 3.13.0 alpha 5 / library / tarfile

[gh-115256](https://github.com/python/cpython/issues/115256): Reading the tarfile attribute on a TarInfo object now emits a DeprecationWarning. CPython itself never consults this attribute; it is set on TarInfos only while the archive is open for writing, and not while reading. Because it forms a needless reference cycle, leaving the handle unclosed after a write can lead to corruption.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
