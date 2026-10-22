# Python 3.13.0 alpha 1 / windows / shutil

[gh-88745](https://github.com/python/cpython/issues/88745): Sped up [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) by leaning on the operating system's `CopyFile2` function. This can produce subtle shifts in the metadata copied alongside certain files, aligning them with ordinary OS behavior.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
