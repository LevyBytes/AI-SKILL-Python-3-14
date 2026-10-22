# tarfile: Archive member types and storage-format constants

tarfile.SYMTYPE

A symbolic link `type`.

 tarfile.CHRTYPE

A character special device `type`.

 tarfile.BLKTYPE

A block special device `type`.

 tarfile.DIRTYPE

A directory `type`.

 tarfile.FIFOTYPE

A FIFO special device `type`.

 tarfile.CONTTYPE

A contiguous file `type`.

 tarfile.GNUTYPE_LONGNAME

A GNU tar longname `type`.

 tarfile.GNUTYPE_LONGLINK

A GNU tar longlink `type`.

 tarfile.GNUTYPE_SPARSE

A GNU tar sparse file `type`.

Every constant below names a tar archive format that the `tarfile` module can produce. Consult the Supported tar formats section for the particulars.

 tarfile.USTAR_FORMAT

POSIX.1-1988 (ustar) format.

 tarfile.GNU_FORMAT

GNU tar format.

 tarfile.PAX_FORMAT

POSIX.1-2001 (pax) format.

 tarfile.DEFAULT_FORMAT

The format used by default when archives are created. At present this is `PAX_FORMAT`.

Changed in version 3.8: For new archives the default switched from `GNU_FORMAT` over to `PAX_FORMAT`.

See also

Module [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile)

Documentation of the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) standard module.

[Archiving operations](https://docs.python.org/3.14/library/shutil.html#archiving-operations)

Documentation of the higher-level archiving facilities provided by the standard [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module.

[GNU tar manual, Basic Tar Format](https://www.gnu.org/software/tar/manual/html_node/Standard.html)

Documentation for tar archive files, including GNU tar extensions.

[Subject index](INDEX.md) · [Previous](tarfile-is-tarfile-to-tarfile-lnktype.md) · [Continue](tarfile-tarfile-class.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
