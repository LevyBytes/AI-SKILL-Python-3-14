# os: macOS and Windows stat-result attributes

On macOS systems, the following attributes may also be present:

 st_rsize

Real size of the file.

 st_creator

Creator of the file.

 st_type

File type.

On Windows systems, the following attributes are present as well:

 st_file_attributes

Windows file attributes: the `dwFileAttributes` member of the `BY_HANDLE_FILE_INFORMATION` structure returned by `GetFileInformationByHandle()`. Consult the `FILE_ATTRIBUTE_* <stat.FILE_ATTRIBUTE_ARCHIVE>` constants in the [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module.

Added in version 3.5.

 st_reparse_tag

Whenever `st_file_attributes` has the [`FILE_ATTRIBUTE_REPARSE_POINT`](https://docs.python.org/3.14/library/stat.html#stat.FILE_ATTRIBUTE_REPARSE_POINT) set, this field holds the tag that identifies the kind of reparse point. Consult the [`IO_REPARSE_TAG_*`](https://docs.python.org/3.14/library/stat.html#stat.IO_REPARSE_TAG_SYMLINK) constants in the [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module.

The standard module [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) supplies functions and constants handy for pulling information out of a `stat` structure. (On Windows, certain items are filled with dummy values.)

For backward compatibility, you can also reach a `stat_result` instance as a tuple holding no fewer than 10 integers that supply the most significant (and portable) members of the `stat` structure, ordered `st_mode`, `st_ino`, `st_dev`, `st_nlink`, `st_uid`, `st_gid`, `st_size`, `st_atime`, `st_mtime`, `st_ctime`. Certain implementations may tack more items onto the end. To stay compatible with older Python versions, reading `stat_result` as a tuple invariably yields integers.

Changed in version 3.5: Windows now yields the file index as `st_ino` where available.

Changed in version 3.7: Added the `st_fstype` member to Solaris/derivatives.

Changed in version 3.8: Added the `st_reparse_tag` member on Windows.

Changed in version 3.8: On Windows, the `st_mode` member now marks special files as `S_IFCHR`, `S_IFIFO` or `S_IFBLK` as appropriate.

Changed in version 3.12: On Windows, `st_ctime` is deprecated. In due course, it will carry the last metadata change time, for consistency with other platforms, but for the moment it still carries creation time. Use `st_birthtime` for the creation time.

On Windows, `st_ino` may now reach up to 128 bits, depending on the file system. Earlier it would stay at or below 64 bits, and larger file identifiers got packed arbitrarily.

On Windows, `st_rdev` no longer yields a value. Earlier it would hold the same as `st_dev`, which was incorrect.

Added the `st_birthtime` member on Windows.

[Subject index](INDEX.md) · [Continue](os-statvfs-to-os-supports-follow-symlinks.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: os.stat_result](os-stat-result-class.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Preceding source contract and version conditions](stat-birthtime-and-platform-fields.md)
