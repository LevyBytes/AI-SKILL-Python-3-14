# Python 3.14.0 beta 3 / library / os

[gh-127081](https://github.com/python/cpython/issues/127081): libc thread safety problems with [`os`](https://docs.python.org/3.14/library/os.html#module-os) were fixed by swapping `getlogin` for the re-entrant `getlogin_r` version.

[gh-135497](https://github.com/python/cpython/issues/135497): [`os.getlogin()`](https://docs.python.org/3.14/library/os.html#os.getlogin) failing for longer usernames on BSD-based platforms was fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
