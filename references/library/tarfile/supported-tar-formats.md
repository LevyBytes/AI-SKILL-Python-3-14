# tarfile — Supported tar formats

### Supported tar formats

The `tarfile` module is able to create three tar formats:

- The POSIX.1-1988 ustar format (`USTAR_FORMAT`). Its filenames can run up to 256 characters at best and its linknames up to 100 characters. A file can be no larger than 8 GiB. This is an old, restricted format, but one that enjoys broad support.

- The GNU tar format (`GNU_FORMAT`). It handles long filenames and linknames, files larger than 8 GiB, and sparse files. On GNU/Linux systems it is the de facto standard. `tarfile` provides full support for the GNU tar long-name extensions, while sparse file support is read-only.

- The POSIX.1-2001 pax format (`PAX_FORMAT`). With virtually no limits, it is the most flexible format. It handles long filenames and linknames, large files, and records pathnames in a portable manner. Today's tar implementations - GNU tar, bsdtar/libarchive, and star among them - fully support the extended *pax* features; certain old or unmaintained libraries may not, yet they ought to handle *pax* archives as though they used the universally supported *ustar* format. For new archives it is the current default format.

It builds on the existing *ustar* format by adding extra headers for information that has no other place to go. Pax headers come in two flavours: extended headers influence only the file header that immediately follows, whereas global headers apply across the entire archive and govern every subsequent file. For portability, every byte of data in a pax header is encoded in *UTF-8*.

A few additional tar variants can be read though not written:

- The ancient V7 format. As the very first tar format, from Unix Seventh Edition, it stores nothing but regular files and directories. Names cannot exceed 100 characters, and there is no user/group name information. Where fields hold non-ASCII characters, some archives carry miscalculated header checksums.

- The SunOS tar extended format. While derived from the POSIX.1-2001 pax format, this format is not compatible with it.

[Subject index](INDEX.md) · [Previous](writing-examples.md) · [Continue](unicode-issues.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
