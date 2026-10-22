# Python 3.13.0 alpha 1 / library / os path

[gh-109782](https://github.com/python/cpython/issues/109782): Guarantee that the signature of [`os.path.isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir) stays the same on every platform. Amin Alaee provided the patch.

[gh-106242](https://github.com/python/cpython/issues/106242): Makes [`os.path.normpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.normpath) cope with embedded null characters without cutting the path short.

[gh-100502](https://github.com/python/cpython/issues/100502): Introduce the `pathlib.PurePath.pathmod` class attribute, which holds whichever [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) implementation drives low-level path operations: either `posixpath` or `ntpath`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
