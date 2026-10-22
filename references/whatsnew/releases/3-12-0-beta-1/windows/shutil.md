# Python 3.12.0 beta 1 / windows / shutil

[gh-82814](https://github.com/python/cpython/issues/82814): Guard against a possible `[Errno 13] Permission denied` that could surface when [`shutil.copystat()`](https://docs.python.org/3.14/library/shutil.html#shutil.copystat) runs under Windows Subsystem for Linux (WSL) over a mounted filesystem, by adding `errno.EACCES` to the errors the internal implementation passes over.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
