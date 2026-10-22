# Python 3.14.5 release candidate 1 / security / shutil

[gh-146581](https://github.com/python/cpython/issues/146581): Patch a [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive) flaw for Windows ZIP files where, if an archived path carried a Windows drive prefix, files could land outside the target tree. Such bad paths are now ignored. Names that include ?..? (for instance ?foo..bar?) are no longer dropped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
