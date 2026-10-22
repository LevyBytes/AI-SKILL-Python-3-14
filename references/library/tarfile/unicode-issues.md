# tarfile — Unicode issues

### Unicode issues

At its inception, the tar format existed so that backups could be written to tape drives, with chief attention paid to retaining file system details. These days, people more often reach for tar archives when distributing files or shipping archives across networks. A shortcoming of that original format — the one every later format builds upon — is that it has no notion of accommodating varied character encodings. Take, for instance, a plain tar archive produced on a *UTF-8* machine: it will not read back correctly on a *Latin-1* machine should it carry non-*ASCII* characters. Any textual metadata — filenames, linknames, and user or group names among them — shows up corrupted. Worse still, an archive offers no means of having its encoding detected automatically. To address exactly this, the pax format came about, keeping its non-ASCII metadata in the universal character encoding *UTF-8*.

How `tarfile` carries out character conversion comes down to the *encoding* and *errors* keyword arguments accepted by the `TarFile` class.

*encoding* sets which character encoding applies to the archive’s metadata. By default this is [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding), falling back to `'ascii'`. According to whether you are reading from or writing to the archive, that metadata gets decoded or else encoded. Should *encoding* be configured improperly, the conversion stands to fail.

The *errors* argument lays out what becomes of characters that resist conversion. You will find its permitted values catalogued in the [Error Handlers](https://docs.python.org/3.14/library/codecs.html#error-handlers) section. Its default is `'surrogateescape'`, the very scheme Python applies to its own file system calls — refer to [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3.14/library/os.html#os-filenames).

With `PAX_FORMAT` archives — which is the default — you typically have no call for *encoding*, since every bit of the metadata is held in *UTF-8*. The *encoding* setting comes into play only in those uncommon situations where binary pax headers get decoded or where strings containing surrogate characters are written out.

[Subject index](INDEX.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
