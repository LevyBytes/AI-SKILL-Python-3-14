# Python 3.13.0 alpha 2 / library / os

[gh-111841](https://github.com/python/cpython/issues/111841): On Windows, stop truncating arguments at an embedded null character within [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv) and [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv).

[gh-90026](https://github.com/python/cpython/issues/90026): Set `USE_XATTRS` on Cygwin, which makes the XATTR-related functions of the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module available there.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
