# shutil: `shutil.get_unpack_formats()`

`shutil.get_unpack_formats()`

Give back a list of every unpacking format on the registry. Each item in the returned sequence is a `(name, extensions, description)` tuple.

Out of the box `shutil` supplies these formats:

- *zip*: ZIP file (decompressing compressed files succeeds only where the matching module is present).

- *tar*: a tar file without compression.

- *gztar*: a gzip-compressed tar-file (where the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module is present).

- *bztar*: a bzip2-compressed tar-file (where the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module is present).

- *xztar*: an xz-compressed tar-file (where the [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) module is present).

- *zstdtar*: a Zstandard-compressed tar-file (where the [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module is present).

Through `register_unpack_format()` you can add new formats or plug your own unpacker into any of the existing ones.

[Subject index](INDEX.md) · [Previous](archive-format-registration-and-removal.md) · [Continue](archiving-example.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Owning module, declaration or section: Archiving operations](shutil-make-archive-to-shutil-get-archive-formats.md)
