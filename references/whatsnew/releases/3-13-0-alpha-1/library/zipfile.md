# Python 3.13.0 alpha 1 / library / zipfile

[gh-106752](https://github.com/python/cpython/issues/106752): Squashed a number of bugs in zipfile.Path: under `zipfile.Path.match()`, Windows separators are no longer respected (they never were supposed to be); repaired the `name`/`suffix`/`suffixes`/`stem` operations for when there is no filename and the Path sits away from the zipfile root; and reworked glob both for speed and for more accurate matching.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
