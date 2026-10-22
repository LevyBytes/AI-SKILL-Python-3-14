# Python 3.14.0 alpha 3 / library / zipfile

[gh-122356](https://github.com/python/cpython/issues/122356): When a file-like object is handed to [`zipfile.is_zipfile()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.is_zipfile), its position is now guaranteed to remain unchanged once the call returns. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
