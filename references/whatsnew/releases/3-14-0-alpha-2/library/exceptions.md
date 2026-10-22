# Python 3.14.0 alpha 2 / library / exceptions

[gh-126223](https://github.com/python/cpython/issues/126223): Throw a [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) rather than a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) whenever `_interpreters.create()` receives an invalid Unicode character.

[gh-118289](https://github.com/python/cpython/issues/118289): `posixpath.realpath()` now throws [`NotADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#NotADirectoryError) once *strict* mode is on and a non-directory path bearing a trailing slash gets passed in.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
