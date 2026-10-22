# Python 3.11.0 beta 1 / library / constants

[gh-90887](https://github.com/python/cpython/issues/90887): Add the `COPYFILE_STAT`, `COPYFILE_ACL` and `COPYFILE_XATTR` constants for `os.fcopyfile()`, which is available on macOs.

[gh-92049](https://github.com/python/cpython/issues/92049): Disallow pickling of the constants `re._constants.SUCCESS` and the like. Pickling formerly succeeded, yet the result was not unpicklable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
