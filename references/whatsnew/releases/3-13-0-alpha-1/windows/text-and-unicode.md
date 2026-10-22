# Python 3.13.0 alpha 1 / windows / text and unicode

[gh-106844](https://github.com/python/cpython/issues/106844): Repaired integer overflow plus truncation by the null character inside `_winapi.LCMapStringEx()`, which has a bearing on `ntpath.normcase()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
