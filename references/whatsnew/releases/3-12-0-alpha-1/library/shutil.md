# Python 3.12.0 alpha 1 / library / shutil

[gh-74696](https://github.com/python/cpython/issues/74696): [`shutil.make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) will no longer briefly switch the current working directory while it builds standard `.zip` or tar archives.

[gh-74696](https://github.com/python/cpython/issues/74696): [`shutil.make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) now forwards the *root_dir* argument on to custom archivers that accept it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
