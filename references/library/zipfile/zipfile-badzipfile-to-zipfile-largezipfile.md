# zipfile: `zipfile.BadZipFile`, `zipfile.BadZipfile`, `zipfile.LargeZipFile`

### `zipfile` — Work with ZIP archives

**Source code:** [Lib/zipfile/](https://github.com/python/cpython/tree/3.14/Lib/zipfile/)

---

ZIP is a widely used standard for archiving and compressing data. With this module you can build, read, write, append to, and enumerate the contents of a ZIP file. To go beyond the basics you'll need to grasp the underlying format, which is described in the [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT).

Multipart ZIP files are not supported here. The module does work with archives built using the ZIP64 extensions — in other words, ZIP files exceeding 4 GiB. Encrypted members inside an archive can be decrypted, though the module offers no way to produce an encrypted file. Because decryption runs in pure Python instead of C, it is exceptionally slow.

To work with compressed archives you need [optional modules](https://docs.python.org/3.14/glossary.html#term-optional-module) like [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib), [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), and [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd). Should any be absent from your particular CPython build, consult the docs supplied by whoever gave you Python (your distributor). Distributors themselves should refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

These are the items the module provides:

 *exception *zipfile.BadZipFile

Raised to signal a malformed ZIP file.

Added in version 3.2.

 *exception *zipfile.BadZipfile

Alias of `BadZipFile`, for compatibility with older Python versions.

Deprecated since version 3.2.

 *exception *zipfile.LargeZipFile

Raised whenever ZIP64 capabilities would be needed for a ZIP file but were never turned on.

[Subject index](INDEX.md) · [Continue](zipfile-zipfile-class.md)
