# Python 3.13.0 alpha 5 / library / buffered stream negative offsets

[gh-95782](https://github.com/python/cpython/issues/95782): Stop `io.BufferedReader.tell()`, `io.BufferedReader.seek()`, `_pyio.BufferedReader.tell()`, `io.BufferedRandom.tell()`, `io.BufferedRandom.seek()` and `_pyio.BufferedRandom.tell()` from ever returning negative offsets.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
