# zipfile: `zipfile.is_zipfile()`, `zipfile.ZIP_STORED`, `zipfile.ZIP_DEFLATED`, `zipfile.ZIP_BZIP2`, `zipfile.ZIP_LZMA`, `zipfile.ZIP_ZSTANDARD`

zipfile.is_zipfile(*filename*)

Yields `True` when *filename* qualifies as a genuine ZIP file according to its magic number, and `False` otherwise. A file or file-like object is also acceptable for *filename*.

Changed in version 3.1: Support for file and file-like objects.

 zipfile.ZIP_STORED

The numeric value denoting a stored (uncompressed) archive member.

 zipfile.ZIP_DEFLATED

The numeric value for the standard ZIP compression method; it depends on the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module.

 zipfile.ZIP_BZIP2

The numeric value for BZIP2 compression; it depends on the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module.

Added in version 3.3.

 zipfile.ZIP_LZMA

The numeric value for LZMA compression; it depends on the [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) module.

Added in version 3.3.

 zipfile.ZIP_ZSTANDARD

The numeric value for Zstandard compression; it depends on the [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module.

Note

APPNOTE 6.3.7 gave Zstandard compression the method ID `20`. To prevent clashes, APPNOTE 6.3.8 reassigned it to method ID `93` and deprecated method ID `20`. The `zipfile` module accepts both IDs when reading for the sake of compatibility, yet it only emits data tagged with method ID `93`.

Added in version 3.14.

Note

Within the ZIP file format specification, bzip2 compression has been covered since 2001, LZMA since 2006, and Zstandard since 2020. Even so, certain tools — among them older Python releases — lack support for these methods and might refuse to process the ZIP file at all, or be unable to extract specific files.

See also

[PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

The ZIP format documented by Phil Katz, who devised both the format itself and its algorithms.

[Info-ZIP Home Page](https://infozip.sourceforge.net/)

Details on the ZIP archive programs and development libraries produced by the Info-ZIP project.

[Subject index](INDEX.md) · [Previous](zipfile-zipinfo-class-to-zipfile-zipinfo-for-archive.md) · [Continue](zipfile-zipfile-class.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md)
