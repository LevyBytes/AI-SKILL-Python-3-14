# Python 3.14.6 final / security / shutil

[gh-149835](https://github.com/python/cpython/issues/149835): [`shutil.move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) now follows symlinks through [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) while verifying that the destination sits within the source directory, which blocks a symlink-driven bypass of that safeguard.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
