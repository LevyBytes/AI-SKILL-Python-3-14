# Python 3.14.3 final / library / os

[gh-143309](https://github.com/python/cpython/issues/143309): On non-Windows platforms, a crash in [`os.execve()`](https://docs.python.org/3.14/library/os.html#os.execve) caused by passing a custom environment mapping that then gets mutated during parsing is now fixed. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
