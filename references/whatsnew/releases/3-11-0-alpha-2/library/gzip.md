# Python 3.11.0 alpha 2 / library / gzip

[bpo-45475](https://bugs.python.org/issue?@action=redirect&bpo=45475): Backed out the iteration optimization for [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile), [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File), and [`lzma.LZMAFile`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMAFile) (refer to [bpo-43787](https://bugs.python.org/issue?@action=redirect&bpo=43787)) since it produced a regression whenever a user iterated them without keeping a reference to them. Inada Naoki wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
