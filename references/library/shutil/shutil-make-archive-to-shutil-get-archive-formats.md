# shutil: `shutil.make_archive()`, `shutil.get_archive_formats()`

### Archiving operations

Added in version 3.2.

Changed in version 3.5: Added support for the *xztar* format.

There are also high-level helpers for building and reading compressed, archived files. They lean on the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) and [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) modules.

`shutil.make_archive(*base_name*, *format*[, *root_dir*[, *base_dir*[, *verbose*[, *dry_run*[, *owner*[, *group*[, *logger*]]]]]]])`

Build an archive file (a zip or tar, say) and give back its name.

*base_name* is the file to create, path included, but stripped of any format-specific extension.

*format* picks the archive format — one of “zip” (when the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module is on hand), “tar”, “gztar” (when the `zlib` module is on hand), “bztar” (when the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module is on hand), “xztar” (when the [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) module is on hand), or “zstdtar” (when the [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module is on hand).

*root_dir* names the directory that becomes the archive’s root; every path within the archive is taken relative to it — for instance, you’d normally chdir into *root_dir* ahead of creating the archive.

*base_dir* is where archiving begins; that is, *base_dir* becomes the shared prefix of all files and directories in the archive. Supply *base_dir* relative to *root_dir*. The section Archiving example with base_dir shows *base_dir* and *root_dir* working in tandem.

Both *root_dir* and *base_dir* fall back to the current directory by default.

With *dry_run* true, no archive gets built, yet the operations that would have run are written to *logger*.

*owner* and *group* come into play while making a tar archive. Left unset, the current owner and group apply.

*logger* has to be an object that conforms to [**PEP 282**](https://peps.python.org/pep-0282/), typically a [`logging.Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instance.

The *verbose* argument goes unused and is deprecated.

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.make_archive` with the arguments `base_name`, `format`, `root_dir`, `base_dir`.

Note

This function loses its thread safety whenever custom archivers registered through `register_archive_format()` don’t accept the *root_dir* argument. In that situation it briefly switches the process’s current working directory over to *root_dir* to carry out the archiving.

Changed in version 3.8: For archives built with `format="tar"`, the up-to-date pax (POSIX.1-2001) format is now applied in place of the old GNU format.

Changed in version 3.10.6: This function is now thread-safe while it builds standard `.zip` and tar archives.

`shutil.get_archive_formats()`

Give back a list of the archiving formats that are supported. Every item in the returned sequence is a `(name, description)` tuple.

Out of the box `shutil` supplies these formats:

- *zip*: ZIP file (when the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module is on hand).

- *tar*: tar file with no compression. New archives use the POSIX.1-2001 pax format.

- *gztar*: a gzip-compressed tar-file (when the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module is on hand).

- *bztar*: a bzip2-compressed tar-file (when the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module is on hand).

- *xztar*: an xz-compressed tar-file (when the [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) module is on hand).

- *zstdtar*: a Zstandard-compressed tar-file (when the [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module is on hand).

Through `register_archive_format()` you can add new formats or plug your own archiver into any of the existing ones.

[Subject index](INDEX.md) · [Previous](rmtree-example.md) · [Continue](archive-format-registration-and-removal.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
