# Python 3.9.0 alpha 1 / library / lzma

[bpo-21872](https://bugs.python.org/issue?@action=redirect&bpo=21872): Repaired [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma): the module had been decompressing data incompletely. With a FORMAT_ALONE format file that lacks an end marker, the trailing few to several dozen bytes occasionally went unwritten. Ma Lin contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
