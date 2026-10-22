# Python 3.14.0 alpha 7 / library / zipfile

[gh-117779](https://github.com/python/cpython/issues/117779): Corrected the reading of duplicated entries by name in [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile). Reading duplicated entries (all but the final one) by `ZipInfo` now produces a warning rather than raising an exception.

[gh-84481](https://github.com/python/cpython/issues/84481): A new `zipfile.ZipFile.data_offset` attribute records the offset to where ZIP data starts within a file, when that is known. If the [`zipfile.ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile) is opened in mode `'w'` or `'x'` and the file underneath has no `tell()` support, the value becomes `None` instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
