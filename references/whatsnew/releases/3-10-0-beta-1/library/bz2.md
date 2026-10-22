# Python 3.10.0 beta 1 / library / bz2

[bpo-43787](https://bugs.python.org/issue?@action=redirect&bpo=43787): Give [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File), [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile), and [`lzma.LZMAFile`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMAFile) an `__iter__()` method. Iterating over them becomes roughly 2x quicker. Inada Naoki wrote the patch.

[bpo-41486](https://bugs.python.org/issue?@action=redirect&bpo=41486): A fresh output-buffer management scheme is now used by the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) / [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) / [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) modules, and a `.readall()` function was added to the `_compression.DecompressReader` class. Together these deliver some speed gains. Ma Lin supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
