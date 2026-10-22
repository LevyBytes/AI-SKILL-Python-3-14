# tarfile: `TarInfo.type`, `TarInfo.sparse`, `TarInfo.replace()`, `TarInfo.isfile()`

TarInfo.type

File type. *type* is generally one of the following constants: `REGTYPE`, `AREGTYPE`, `LNKTYPE`, `SYMTYPE`, `DIRTYPE`, `FIFOTYPE`, `CONTTYPE`, `CHRTYPE`, `BLKTYPE`, `GNUTYPE_SPARSE`. For a more convenient way to find out a `TarInfo` object's type, turn to the `is*()` methods below.

 TarInfo.linkname*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

Name of the target file name, which appears only in `TarInfo` objects whose type is `LNKTYPE` or `SYMTYPE`.

With symbolic links (`SYMTYPE`), the *linkname* is taken relative to the directory holding the link. With hard links (`LNKTYPE`), the *linkname* is taken relative to the archive's root.

 TarInfo.uid*: [int](https://docs.python.org/3.14/library/functions.html#int)*

User ID of the user who originally stored this member.

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

 TarInfo.gid*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Group ID of the user who originally stored this member.

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

 TarInfo.uname*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

User name.

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

 TarInfo.gname*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

Group name.

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

 TarInfo.chksum*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Header checksum.

 TarInfo.devmajor*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Device major number.

 TarInfo.devminor*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Device minor number.

 TarInfo.offset*: [int](https://docs.python.org/3.14/library/functions.html#int)*

The tar header starts here.

 TarInfo.offset_data*: [int](https://docs.python.org/3.14/library/functions.html#int)*

The file's data starts here.

 TarInfo.sparse

Sparse member information.

 TarInfo.pax_headers*: [dict](https://docs.python.org/3.14/library/stdtypes.html#dict)*

A dictionary containing key-value pairs of an associated pax extended header.

 TarInfo.replace(*name=...*, *mtime=...*, *mode=...*, *linkname=...*, *uid=...*, *gid=...*, *uname=...*, *gname=...*, *deep=True*)

Added in version 3.12.

Hand back a *new* copy of the `TarInfo` object in which the supplied attributes have been altered. For instance, to obtain a `TarInfo` whose group name reads `'staff'`, use:

```python
new_tarinfo = old_tarinfo.replace(gname='staff')

```

A deep copy is produced by default. If *deep* is false, the copy stays shallow, meaning `pax_headers` and any custom attributes remain shared with the original `TarInfo` object.

A `TarInfo` object also provides some convenient query methods:

 TarInfo.isfile()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the `TarInfo` object is a regular file.

[Subject index](INDEX.md) · [Previous](tarinfo-tobuf.md) · [Continue](tarinfo-isreg-to-tarinfo-isdev.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Owning module, declaration or section: tarfile.TarInfo](tarfile-tarinfo-class.md) · [Owning module, declaration or section: TarInfo Objects](tarfile-tarinfo-class.md)
