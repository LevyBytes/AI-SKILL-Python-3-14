# Python 3.13.0 alpha 3 / macos / dbm

[gh-74573](https://github.com/python/cpython/issues/74573): Record that [`dbm.ndbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) may quietly damage DBM files during updates past undocumented platform ceilings, and can fault (segmentation fault) while reading one of those corrupted files. (FB8919203)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
