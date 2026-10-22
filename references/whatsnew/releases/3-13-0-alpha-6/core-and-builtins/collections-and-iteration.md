# Python 3.13.0 alpha 6 / core and builtins / collections and iteration

[gh-116554](https://github.com/python/cpython/issues/116554): `list.sort()` now takes advantage of additional partial-ordering situations, especially long descending runs containing sub-runs of identical values. These get treated as one run (formerly, every block of repeated values spawned a brand-new run).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
