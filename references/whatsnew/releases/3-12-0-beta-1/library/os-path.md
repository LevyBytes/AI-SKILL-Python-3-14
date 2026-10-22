# Python 3.12.0 beta 1 / library / os path

[gh-103220](https://github.com/python/cpython/issues/103220): Repair a case where [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) inserted a slash while joining onto an incomplete UNC drive that ended in a trailing slash on Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
