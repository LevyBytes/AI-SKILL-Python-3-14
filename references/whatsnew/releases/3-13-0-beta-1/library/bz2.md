# Python 3.13.0 beta 1 / library / bz2

[gh-115961](https://github.com/python/cpython/issues/115961): The `name` and `mode` attributes were added for compressed and archived file-like objects across the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) and [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) modules. For [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile), the `mode` attribute switched from an integer (`1` or `2`) to a string (`'rb'` or `'wb'`). The readable file-like object handed back by [`zipfile.ZipFile.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) likewise saw its `mode` attribute move from `'r'` to `'rb'`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
