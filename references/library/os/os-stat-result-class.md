# os: `os.stat_result`

*class *os.stat_result

Object whose attributes line up roughly with the members of the `stat` structure. It serves as the result of `os.stat()`, `os.fstat()` and `os.lstat()`.

Attributes:

 st_mode

File mode: file type and file mode bits (permissions).

 st_ino

Platform dependent, but when non-zero, uniquely identifies the file for a given value of `st_dev`. Typically:

- the inode number on Unix,

- the [file index](https://msdn.microsoft.com/en-us/library/aa363788) on Windows

 st_dev

Identifier of the device on which this file resides.

 st_nlink

Number of hard links.

 st_uid

User identifier of the file owner.

 st_gid

Group identifier of the file owner.

 st_size

Size of the file in bytes, where it happens to be a regular file or a symbolic link. For a symbolic link, the size equals the length of the pathname stored in it, minus any terminating null byte.

Timestamps:

 st_atime

Time of most recent access expressed in seconds.

 st_mtime

Time of most recent content modification expressed in seconds.

 st_ctime

Time of most recent metadata change expressed in seconds.

Changed in version 3.12: On Windows, `st_ctime` is deprecated. For the file creation time, turn to `st_birthtime`. In later releases, `st_ctime` will carry the time of the most recent metadata change, as on other platforms.

 st_atime_ns

Time of most recent access expressed in nanoseconds as an integer.

Added in version 3.3.

 st_mtime_ns

Time of most recent content modification expressed in nanoseconds as an integer.

Added in version 3.3.

 st_ctime_ns

Time of most recent metadata change expressed in nanoseconds as an integer.

Added in version 3.3.

Changed in version 3.12: On Windows, `st_ctime_ns` is deprecated. For the file creation time, turn to `st_birthtime_ns`. In later releases, `st_ctime` will carry the time of the most recent metadata change, as on other platforms.

 st_birthtime

Time of file creation expressed in seconds. This attribute is not always present, and may raise [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Changed in version 3.12: `st_birthtime` is now available on Windows.

[Subject index](INDEX.md) · [Previous](os-stat.md) · [Continue](stat-birthtime-and-platform-fields.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
