# Python 3.14.0 alpha 5 / library / profile

[gh-118761](https://github.com/python/cpython/issues/118761): Trim as much as 20% off the import cost of [`pstats`](https://docs.python.org/3.14/library/profile.html#module-pstats) and [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) by stripping out needless [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) imports. Bénédikt Tran contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
