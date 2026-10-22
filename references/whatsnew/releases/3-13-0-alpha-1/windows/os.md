# Python 3.13.0 alpha 1 / windows / os

[gh-104820](https://github.com/python/cpython/issues/104820): Repairs [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat) plus the related calls when the underlying file system cannot honor file ID lookups. FAT32 and exFAT fall into that category.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
