# Python 3.13.0 alpha 6 / windows / os

[gh-117267](https://github.com/python/cpython/issues/117267): Keep `DirEntry.stat().st_ctime` lined up with [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) throughout the deprecation window for `st_ctime` by carrying the same value that `st_birthtime` does. Once that window closes, `st_ctime` becomes the metadata change time (or stops being reachable via `DirEntry`), and the creation time will live solely in `st_birthtime`.

[gh-116195](https://github.com/python/cpython/issues/116195): Speeds up [`os.getppid()`](https://docs.python.org/3.14/library/os.html#os.getppid) by reaching for an alternate system API where one exists. vxiiduu contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
