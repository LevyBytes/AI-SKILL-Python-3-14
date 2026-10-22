# Python 3.13.0 beta 1 / library / os path

[gh-117503](https://github.com/python/cpython/issues/117503): Adds handling for non-ASCII user names within bytes paths passed to [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) under Posix.

[gh-117394](https://github.com/python/cpython/issues/117394): [`os.path.ismount()`](https://docs.python.org/3.14/library/os.path.html#os.path.ismount) now runs 2-3 times faster provided the user holds the needed permissions.

[gh-102511](https://github.com/python/cpython/issues/102511): Fixes [`os.path.normpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.normpath) on Windows for UNC paths. A native implementation also accelerates [`os.path.splitroot()`](https://docs.python.org/3.14/library/os.path.html#os.path.splitroot).

[gh-117641](https://github.com/python/cpython/issues/117641): Accelerates [`os.path.commonpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.commonpath) on Unix.

[gh-117636](https://github.com/python/cpython/issues/117636): Accelerates [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join).

[gh-117607](https://github.com/python/cpython/issues/117607): Accelerates [`os.path.relpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.relpath).

[gh-117546](https://github.com/python/cpython/issues/117546): Corrects a case where [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) quit resolving symlinks once it hit a symlink loop under POSIX.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
