# Python 3.10.0 beta 1 / library / gzip

[bpo-43785](https://bugs.python.org/issue?@action=redirect&bpo=43785): Speed up `bz2.BZ2File` by taking the RLock out of BZ2File. That leaves BZ2File thread unsafe when several readers or writers act at once, matching how its counterparts in [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) and [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) have always behaved. Inada Naoki wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
