# Python 3.14.0 alpha 5 / library / pyio fileio readall allocates resizes populates data buffer very algorithm io fileio readall

[gh-129005](https://github.com/python/cpython/issues/129005): `_pyio.FileIO.readall()` now allocates, resizes, and populates a data buffer with the very algorithm that `_io.FileIO.readall()` employs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
