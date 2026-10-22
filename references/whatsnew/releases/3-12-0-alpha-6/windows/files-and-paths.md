# Python 3.12.0 alpha 6 / windows / files and paths

[gh-101196](https://github.com/python/cpython/issues/101196): On Windows the functions `os.path.isdir`, `os.path.isfile`, `os.path.islink` and `os.path.exists` gain a 13% to 28% speedup, achieved by issuing fewer Win32 API calls.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
