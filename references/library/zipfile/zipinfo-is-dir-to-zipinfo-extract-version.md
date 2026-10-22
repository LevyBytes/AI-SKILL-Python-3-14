# zipfile: `ZipInfo.from_file()`, `ZipInfo.is_dir()`, `ZipInfo.filename`, `ZipInfo.date_time`, `ZipInfo.compress_type`, `ZipInfo.comment`, `ZipInfo.extra`, `ZipInfo.create_system`, `ZipInfo.create_version`, `ZipInfo.extract_version`

### ZipInfo objects

Instances of the `ZipInfo` class come back from the `getinfo()` and `infolist()` methods of `ZipFile` objects. Every object holds the details about one single member of the ZIP archive.

A single classmethod exists to produce a `ZipInfo` instance for a filesystem file:

 *classmethod *ZipInfo.from_file(*filename*, *arcname=None*, ***, *strict_timestamps=True*)

Build a `ZipInfo` instance representing a filesystem file, getting it ready to be added into a zip file.

*filename* ought to give the path leading to a filesystem file or directory.

Where *arcname* is given, that serves as the name within the archive. Where *arcname* is left out, the name matches *filename*, except with any drive letter and leading path separators stripped off.

The *strict_timestamps* argument, once set to `False`, makes it possible to zip files older than 1980-01-01 at the price of pinning the timestamp to 1980-01-01. The same thing happens with files newer than 2107-12-31, whose timestamp likewise gets pinned to the limit.

Added in version 3.6.

Changed in version 3.6.2: The *filename* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: Added the *strict_timestamps* keyword-only parameter.

Instances have the following methods and attributes:

 ZipInfo.is_dir()

Return `True` if this archive member is a directory.

This relies on the entry's name: directories ought always to close with `/`.

Added in version 3.6.

 ZipInfo.filename

Name of the file in the archive.

 ZipInfo.date_time

When the archive member was last modified, given as time and date. This takes the form of a tuple of six values standing for the “last [modified] file time” and “last [modified] file date” fields drawn from the ZIP file's central directory.

The tuple contains:

| Index | Value |
| --- | --- |
| `0` | Year (>= 1980) |
| `1` | Month (one-based) |
| `2` | Day of month (one-based) |
| `3` | Hours (zero-based) |
| `4` | Minutes (zero-based) |
| `5` | Seconds (zero-based) |

Note

Across different locations (central directory, extra fields for NTFS/UNIX systems, and so on), the ZIP format carries several timestamp fields. What this attribute specifically returns is the timestamp drawn from the central directory. In ZIP files the central directory timestamp format cannot represent timestamps earlier than 1980. Although certain extra field formats (UNIX timestamps among them) are able to express earlier dates, this attribute returns the central directory timestamp alone.

To line up with the behavior of other zip tools, the central directory timestamp is read as standing for local time rather than UTC time.

 ZipInfo.compress_type

Type of compression for the archive member.

 ZipInfo.comment

Comment for the individual archive member as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

 ZipInfo.extra

Expansion field data. The [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) carries a few remarks about the internal layout of the data held within this [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

 ZipInfo.create_system

System which created ZIP archive.

 ZipInfo.create_version

PKZIP version which created ZIP archive.

 ZipInfo.extract_version

PKZIP version needed to extract archive.

[Subject index](INDEX.md) · [Previous](zipfile-pyzipfile-writepy.md) · [Continue](zipinfo-reserved-to-zipinfo-file-size.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md)
