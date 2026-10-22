# tarfile: `TarFile.gettarinfo()`, `TarFile.close()`

Append the `TarInfo` object *tarinfo* into the archive. When *tarinfo* describes a regular file whose size is non-zero, supply a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file) through the *fileobj* argument; `tarinfo.size` bytes are then read out of it and stored in the archive. `TarInfo` objects may be built by hand, or produced via `gettarinfo()`.

Changed in version 3.13: for regular files of non-zero size, *fileobj* is now required.

 TarFile.gettarinfo(*name=None*, *arcname=None*, *fileobj=None*)

Build a `TarInfo` object out of what [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) (or an equivalent call) reports for a file that already exists. The file is identified either by *name* or by a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *fileobj* that carries a file descriptor. *name* is allowed to be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). When *arcname* is provided, it gives the file a different name inside the archive; otherwise the name comes from *fileobj*'s [`name`](https://docs.python.org/3.14/library/io.html#io.FileIO.name) attribute or from the *name* argument. The name ought to be a text string.

A few of the `TarInfo`'s attributes can be adjusted before you pass it to `addfile()`. When the file object is not a plain file object sitting at the start of the file, fields such as `size` might require adjustment. Objects like [`GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) fall into this category. You can change the `name` too, and if you do, *arcname* may just be a placeholder string.

Changed in version 3.6: The *name* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 TarFile.close()

Close the `TarFile`. When writing, the archive is finished off with two trailing zero blocks.

 TarFile.pax_headers*: [dict](https://docs.python.org/3.14/library/stdtypes.html#dict)*

A dictionary containing key-value pairs of pax global headers.

[Subject index](INDEX.md) · [Continue](tarfile-tarinfo-class.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Owning module, declaration or section: tarfile.TarFile](tarfile-tarfile-class.md) · [Owning module, declaration or section: TarFile Objects](tarfile-tarfile-class.md) · [Owning module, declaration or section: TarFile.addfile](tarfile-extractfile-to-tarfile-addfile.md) · [Preceding source contract and version conditions](tarfile-extractfile-to-tarfile-addfile.md)
