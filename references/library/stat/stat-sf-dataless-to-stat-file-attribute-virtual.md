# stat: Dataless files and Windows file attributes

stat.SF_DATALESS

The file is a dataless object (macOS 10.15+)

Added in version 3.13.

See the *BSD or macOS systems man page *[chflags(2)](https://manpages.debian.org/chflags(2))* for more information.

Under Windows, these file-attribute constants let you test bits within the `st_file_attributes` member that [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) returns. Consult the [Windows API documentation](https://msdn.microsoft.com/en-us/library/windows/desktop/gg258117.aspx) for fuller explanations of what each constant signifies.

 stat.FILE_ATTRIBUTE_ARCHIVE

 stat.FILE_ATTRIBUTE_COMPRESSED

 stat.FILE_ATTRIBUTE_DEVICE

 stat.FILE_ATTRIBUTE_DIRECTORY

 stat.FILE_ATTRIBUTE_ENCRYPTED

 stat.FILE_ATTRIBUTE_HIDDEN

 stat.FILE_ATTRIBUTE_INTEGRITY_STREAM

 stat.FILE_ATTRIBUTE_NORMAL

 stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED

 stat.FILE_ATTRIBUTE_NO_SCRUB_DATA

 stat.FILE_ATTRIBUTE_OFFLINE

 stat.FILE_ATTRIBUTE_READONLY

 stat.FILE_ATTRIBUTE_REPARSE_POINT

 stat.FILE_ATTRIBUTE_SPARSE_FILE

 stat.FILE_ATTRIBUTE_SYSTEM

 stat.FILE_ATTRIBUTE_TEMPORARY

 stat.FILE_ATTRIBUTE_VIRTUAL

Added in version 3.5.

Under Windows, the constants below can be matched against the `st_reparse_tag` member that [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) returns. They cover the familiar cases, though the list does not claim to be complete.

[Subject index](INDEX.md) · [Previous](stat-uf-nounlink-to-stat-sf-firmlink.md) · [Continue](windows-reparse-tag-constants.md) · [Owning module, declaration or section: stat](stat-s-isdir-to-stat-s-imode.md)
