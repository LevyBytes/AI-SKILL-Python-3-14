# zipfile: `ZipFile.read()`, `ZipFile.testzip()`, `ZipFile.write()`, `ZipFile.writestr()`, `ZipFile.mkdir()`, `ZipFile.filename`, `ZipFile.debug`, `ZipFile.comment`

ZipFile.read(*name*, *pwd=None*)

Hand back the bytes of the file *name* within the archive. Here *name* is the file's name in the archive, or a `ZipInfo` object. The archive has to be open for reading or appending. The *pwd* argument is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object holding the password for encrypted files, and when provided it supersedes whatever default password was registered through `setpassword()`. Invoking `read()` on a ZipFile whose compression method is anything other than `ZIP_STORED`, `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or `ZIP_ZSTANDARD` raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError). An error likewise arises when the matching compression module isn't present.

Changed in version 3.6: Calling `read()` against a closed ZipFile now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); what came up before was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 ZipFile.testzip()

Go through every file in the archive, verifying its CRC and file headers. Return the name belonging to the first corrupt file, or `None` if there is none.

Changed in version 3.6: Invoking `testzip()` on a closed ZipFile now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); beforehand the outcome was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 ZipFile.write(*filename*, *arcname=None*, *compress_type=None*, *compresslevel=None*)

Add the file called *filename* to the archive under the archive name *arcname* (which defaults to *filename* itself, minus any drive letter and with leading path separators stripped). When supplied, *compress_type* takes precedence over the *compression* value handed to the constructor for this new entry. In the same way, *compresslevel* overrides the constructor when supplied. The archive has to be open with mode `'w'`, `'x'`, or `'a'`.

Note

Historically the ZIP file standard left the metadata encoding unspecified, though it firmly recommended CP437 (the original IBM PC encoding) for interoperability. Newer revisions permit UTF-8 (only). In this module, member names get written using UTF-8 automatically whenever they hold any non-ASCII characters. Writing member names in any encoding besides ASCII or UTF-8 isn't possible.

Note

Names within the archive ought to be relative to its root — meaning they must not begin with a path separator.

Note

When `arcname` (or `filename`, where `arcname` isn't supplied) holds a null byte, the file's name in the archive gets cut off at that null byte.

Note

Should the filename carry a leading slash, certain zip programs on Windows systems may be unable to open the resulting archive.

Changed in version 3.6: Calling `write()` on a closed ZipFile, or one opened with mode `'r'`, now produces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); the earlier result was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 ZipFile.writestr(*zinfo_or_arcname*, *data*, *compress_type=None*, *compresslevel=None*)

Put a file into the archive. Its contents are *data*, supplied as either a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) instance; a `str` gets encoded as UTF-8 beforehand. The *zinfo_or_arcname* argument is either the name the file will carry in the archive, or a `ZipInfo` instance. For an instance, you must at minimum provide the filename, date, and time. For a name, the date and time default to right now. The archive has to be opened with mode `'w'`, `'x'`, or `'a'`.

When supplied, *compress_type* takes precedence over the *compression* value passed to the constructor for this new entry, or over the one in *zinfo_or_arcname* (where that is a `ZipInfo` instance). In the same way, *compresslevel* overrides the constructor when supplied.

Note

Where a `ZipInfo` instance serves as the *zinfo_or_arcname* parameter, the compression applied is whatever the *compress_type* member of that `ZipInfo` instance names. The `ZipInfo` constructor leaves this member at `ZIP_STORED` by default.

Changed in version 3.2: The *compress_type* argument.

Changed in version 3.6: Calling `writestr()` on a closed ZipFile, or one made with mode `'r'`, now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); formerly it was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Changed in version 3.14: The `SOURCE_DATE_EPOCH` environment variable is now honored. When it has a value, that value — rather than the present time — becomes the modification timestamp on the file placed into the ZIP archive.

 ZipFile.mkdir(*zinfo_or_directory*, *mode=511*)

Make a directory within the archive. When *zinfo_or_directory* is a string, a directory gets created inside the archive using the mode named by the *mode* argument. When instead *zinfo_or_directory* is a `ZipInfo` instance, the *mode* argument has no effect.

For this, the archive needs to have been opened under mode `'w'`, `'x'`, or `'a'`.

Added in version 3.11.

The following data attributes are also available:

 ZipFile.filename

Name of the ZIP file.

 ZipFile.debug

How much debug output to produce. Acceptable values run from `0` (the default, meaning no output) up to `3` (the maximum output). The debugging text goes to `sys.stdout`.

 ZipFile.comment

The comment attached to the ZIP file, held as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. When you assign a comment to a `ZipFile` instance opened with mode `'w'`, `'x'`, or `'a'`, keep it within 65535 bytes. Anything past that length gets truncated.

[Subject index](INDEX.md) · [Previous](zipfile-close-to-zipfile-setpassword.md) · [Continue](zipfile-path-class.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Owning module, declaration or section: zipfile.ZipFile](zipfile-zipfile-class.md) · [Owning module, declaration or section: ZipFile objects](zipfile-zipfile-class.md)
