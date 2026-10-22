# Python 3.14.6 final / library / zipfile

[gh-84353](https://github.com/python/cpython/issues/84353): Retain non-UTF-8 encoded filenames while appending onto a [`zipfile.ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile). Formerly, non-ASCII names held in a legacy encoding (lacking the UTF-8 flag bit) risked corruption once the central directory got rewritten: they were read as cp437 then re-saved as UTF-8.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
