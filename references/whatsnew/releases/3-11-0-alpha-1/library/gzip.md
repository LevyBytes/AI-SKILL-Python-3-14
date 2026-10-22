# Python 3.11.0 alpha 1 / library / gzip

[bpo-43613](https://bugs.python.org/issue?@action=redirect&bpo=43613): Sped up [`gzip.compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) along with [`gzip.decompress()`](https://docs.python.org/3.14/library/gzip.html#gzip.decompress) by handling the whole compression and decompression in one in-memory pass rather than streaming it piece by piece.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
