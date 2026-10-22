# Python 3.14.0 alpha 6 / library / zipapp

[gh-130379](https://github.com/python/cpython/issues/130379): The zipapp module now figures out which files belong in the archive ahead of creating it. That sidesteps inadvertently pulling in the target while it gets created inside the source directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
