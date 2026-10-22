# zipfile: `zipfile.ZipFile`

*class *zipfile.ZipFile

The class used to read from and write to ZIP files. Constructor specifics appear in the ZipFile objects section.

### ZipFile objects

 *class *zipfile.ZipFile(*file*, *mode='r'*, *compression=ZIP_STORED*, *allowZip64=True*, *compresslevel=None*, ***, *strict_timestamps=True*, *metadata_encoding=None*)

Open a ZIP file; the *file* argument may be a filesystem path given as a string, a file-like object, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Use the *mode* parameter as follows: `'r'` reads an existing file, `'w'` truncates and writes a fresh file, `'a'` appends onto an existing file, and `'x'` exclusively creates and writes a new file. With *mode* `'x'`, if *file* points at a file that already exists, a [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) results. With *mode* `'a'`, if *file* names an existing ZIP file, more files get appended into it. Should *file* not actually be a ZIP file, a fresh ZIP archive gets tacked onto the end of the file. The intent here is to attach a ZIP archive to some other file (for instance, `python.exe`). With *mode* `'a'`, if no file exists yet, one is created. Under *mode* `'r'` or `'a'`, the file needs to be seekable.

*compression* is the ZIP compression method applied while writing the archive; valid choices are `ZIP_STORED`, `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or `ZIP_ZSTANDARD`, and anything else triggers a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError). When `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or `ZIP_ZSTANDARD` is requested yet its backing module ([`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib), [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), or [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd)) can't be found, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised. The default is `ZIP_STORED`.

When *allowZip64* is `True` (its default), zipfile produces ZIP files relying on the ZIP64 extensions once the zipfile grows past 4 GiB. When it is `false`, `zipfile` throws an exception in any case where the ZIP file would call for ZIP64 extensions.

The *compresslevel* parameter sets the compression level applied as files are written into the archive. It does nothing for `ZIP_STORED` or `ZIP_LZMA`. For `ZIP_DEFLATED`, the integers `0` through `9` are valid (consult [`zlib`](https://docs.python.org/3.14/library/zlib.html#zlib.compressobj) for details). For `ZIP_BZIP2`, the integers `1` through `9` are valid (consult [`bz2`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) for details). For `ZIP_ZSTANDARD`, the integers `-131072` through `22` are typically valid (consult [`CompressionParameter.compression_level`](https://docs.python.org/3.14/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level) to learn how to fetch the permitted values and what they signify).

Setting the *strict_timestamps* argument to `False` permits zipping files dated before 1980-01-01, with the trade-off that their timestamp gets pinned to 1980-01-01. The same thing happens to files dated after 2107-12-31, whose timestamp is clamped to that boundary.

While mode is `'r'`, you can point *metadata_encoding* at a codec name, and that codec will decode metadata — for example member names and ZIP comments.

Should the file be created under mode `'w'`, `'x'`, or `'a'` and then `closed` without any files having been added, the proper ZIP structures representing an empty archive are written into the file.

Because ZipFile doubles as a context manager, it works with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Below, *myzip* gets closed once the suite under the `with` statement completes — even should an exception be raised:

```python
with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')

```

Note

*metadata_encoding* applies across the whole ZipFile instance. There's no way to configure it per member.

This attribute exists as a fallback for older implementations that emit archives whose names follow the current locale encoding or code page (chiefly on Windows). Per the .ZIP standard, an archive-header flag declares the metadata encoding as either IBM code page (the default) or UTF-8. That flag wins out over *metadata_encoding*, a Python-only addition.

Changed in version 3.2: Gained the option of treating `ZipFile` as a context manager.

Changed in version 3.3: Gained support for [`bzip2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) and [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) compression.

Changed in version 3.4: ZIP64 extensions are turned on by default.

Changed in version 3.5: Gained the ability to write into unseekable streams. Gained the `'x'` mode.

Changed in version 3.6: Earlier, an ordinary [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) came up when compression values weren't recognized.

Changed in version 3.6.2: The *file* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: Add the *compresslevel* parameter.

Changed in version 3.8: The *strict_timestamps* keyword-only parameter.

Changed in version 3.11: Gained the ability to declare member-name encoding when reading metadata out of the zipfile’s directory and file headers.

[Subject index](INDEX.md) · [Previous](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Continue](zipfile-path-class.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Previous](zipfile-is-zipfile-to-zipfile-zip-zstandard.md) · [Continue](zipfile-close-to-zipfile-setpassword.md)
