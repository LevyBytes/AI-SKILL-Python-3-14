# tarfile: `tarfile.open()`

tarfile.open(*name=None*, *mode='r'*, *fileobj=None*, *bufsize=10240*, ***kwargs*)

Hand back a `TarFile` object for the pathname *name*. The TarFile Objects section covers `TarFile` objects in depth, along with the keyword arguments they accept.

The *mode* value must be a string shaped like `'filemode[:compression]'`, and `'r'` is the default. Every supported mode combination appears below:

| mode | action |
| --- | --- |
| `'r'` or `'r:*'` | Open for reading with transparent compression (recommended). |
| `'r:'` | Open for reading exclusively without compression. |
| `'r:gz'` | Open for reading with gzip compression. |
| `'r:bz2'` | Open for reading with bzip2 compression. |
| `'r:xz'` | Open for reading with lzma compression. |
| `'r:zst'` | Open for reading with Zstandard compression. |
| `'x'` or `'x:'` | Exclusively create an uncompressed tarfile; should one already exist, raise `FileExistsError`. |
| `'x:gz'` | Build a tarfile under gzip compression; should one already exist, raise `FileExistsError`. |
| `'x:bz2'` | Build a tarfile under bzip2 compression; should one already exist, raise `FileExistsError`. |
| `'x:xz'` | Build a tarfile under lzma compression; should one already exist, raise `FileExistsError`. |
| `'x:zst'` | Build a tarfile under Zstandard compression; should one already exist, raise `FileExistsError`. |
| `'a'` or `'a:'` | Open to append without any compression; when the file is absent, it gets created. |
| `'w'` or `'w:'` | Open for uncompressed writing. |
| `'w:gz'` | Open for gzip compressed writing. |
| `'w:bz2'` | Open for bzip2 compressed writing. |
| `'w:xz'` | Open for lzma compressed writing. |
| `'w:zst'` | Open for Zstandard compressed writing. |

Keep in mind that `'a:gz'`, `'a:bz2'` or `'a:xz'` is not possible. Whenever *mode* cannot open a given (compressed) file for reading, `ReadError` results. Pass *mode* `'r'` to sidestep this. When a compression method has no support, `CompressionError` results instead.

When *fileobj* is given, it stands in for a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) opened against *name* in binary mode. The expectation is that it sits at position 0.

Across the modes `'w:gz'`, `'x:gz'`, `'w|gz'`, `'w:bz2'`, `'x:bz2'`, `'w|bz2'`, a *compresslevel* keyword argument (default `9`) may be handed to `tarfile.open()` to dictate the file's compression level.

Across the modes `'w:xz'`, `'x:xz'` and `'w|xz'`, a *preset* keyword argument may be handed to `tarfile.open()` to dictate the file's compression level.

Across the modes `'w:zst'`, `'x:zst'` and `'w|zst'`, a *level* keyword argument may be handed to `tarfile.open()` to dictate the file's compression level. You may additionally pass an *options* keyword argument that carries the advanced Zstandard compression parameters laid out in [`CompressionParameter`](https://docs.python.org/3.14/library/compression.zstd.html#compression.zstd.CompressionParameter). A *zstd_dict* keyword argument is also accepted, supplying a [`ZstdDict`](https://docs.python.org/3.14/library/compression.zstd.html#compression.zstd.ZstdDict) — a Zstandard dictionary that sharpens compression when the data volume is small.

A second *mode* form also exists for special purposes: `'filemode|[compression]'`. Here `tarfile.open()` returns a `TarFile` object that handles its data as a stream of blocks, performing no random seeks on the file. When given, *fileobj* may be any object offering a [`read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read) or [`write()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.write) method (matched to the *mode*) that handles bytes. The *bufsize* argument fixes the blocksize, defaulting to `20 * 512` bytes. Use this variant alongside something like `sys.stdin.buffer`, a socket [file object](https://docs.python.org/3.14/glossary.html#term-file-object) or a tape device. Note, however, that random access is off limits for such a `TarFile` object, see Examples. The modes on offer right now are:

| Mode | Action |
| --- | --- |
| `'r|*'` | Open a *stream* of tar blocks for reading with transparent compression. |
| `'r|'` | Open a *stream* of uncompressed tar blocks for reading. |
| `'r|gz'` | Open a gzip compressed *stream* for reading. |
| `'r|bz2'` | Open a bzip2 compressed *stream* for reading. |
| `'r|xz'` | Open an lzma compressed *stream* for reading. |
| `'r|zst'` | Open a Zstandard compressed *stream* for reading. |
| `'w|'` | Open an uncompressed *stream* for writing. |
| `'w|gz'` | Open a gzip compressed *stream* for writing. |
| `'w|bz2'` | Open a bzip2 compressed *stream* for writing. |
| `'w|xz'` | Open an lzma compressed *stream* for writing. |
| `'w|zst'` | Open a Zstandard compressed *stream* for writing. |

Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

Changed in version 3.6: The *name* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: Streams now honor the *compresslevel* keyword argument too.

Changed in version 3.14: Streams now honor the *preset* keyword argument too.

[Subject index](INDEX.md) · [Previous](tarfile-read-and-write-tar-archive-files.md) · [Continue](tarfile-tarfile-class.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
