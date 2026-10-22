# Python 3.13.0 alpha 2 / windows / os

[gh-111856](https://github.com/python/cpython/issues/111856): Repairs [`fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat) on file systems lacking support for file ID requests, FAT32 and exFAT among them.

[gh-111293](https://github.com/python/cpython/issues/111293): Stop [`os.DirEntry.inode`](https://docs.python.org/3.14/library/os.html#os.DirEntry.inode) from discarding the upper 64 bits of a file id on certain Windows filesystems.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
