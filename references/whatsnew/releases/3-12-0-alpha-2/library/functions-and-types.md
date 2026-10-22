# Python 3.12.0 alpha 2 / library / functions and types

[gh-98999](https://github.com/python/cpython/issues/98999): `_pyio` now matches `_io` by raising `ValueError` whenever a method runs against a buffer that has been closed.

[gh-98793](https://github.com/python/cpython/issues/98793): Correct the argument typechecks performed by the `_overlapped.WSAConnect()` and `_overlapped.Overlapped.WSASendTo()` functions.

[gh-98086](https://github.com/python/cpython/issues/98086): Guarantee that `patch.dict()` works when applied to async functions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
