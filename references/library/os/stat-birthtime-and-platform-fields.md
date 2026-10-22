# os: File birth time and platform stat extensions

st_birthtime_ns

Creation time of the file given in nanoseconds as an integer. Not every system provides this attribute, and accessing it may raise [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Added in version 3.12.

Note

The precise meaning and resolution of the `st_atime`, `st_mtime`, `st_ctime` and `st_birthtime` attributes hinge on the operating system and the file system. For instance, on Windows machines running the FAT32 file systems, `st_mtime` carries 2-second resolution, whereas `st_atime` carries only 1-day resolution. Consult your operating system documentation for the particulars.

In the same way, although `st_atime_ns`, `st_mtime_ns`, `st_ctime_ns` and `st_birthtime_ns` are always expressed in nanoseconds, plenty of systems do not deliver nanosecond precision. On systems that do deliver nanosecond precision, the floating-point object used to hold `st_atime`, `st_mtime`, `st_ctime` and `st_birthtime` cannot keep all of it, and so will be slightly inexact. Should you need the exact timestamps you should always use `st_atime_ns`, `st_mtime_ns`, `st_ctime_ns` and `st_birthtime_ns`.

On a few Unix systems (Linux among them), these further attributes may also be present:

 st_blocks

Number of 512-byte blocks allocated for file. This may fall below `st_size`/512 when the file holds holes.

 st_blksize

"Preferred" blocksize for efficient file system I/O. Should you write to a file in smaller chunks, an inefficient read-modify-rewrite may result.

 st_rdev

Type of device when an inode device.

 st_flags

User defined flags for file.

On other Unix systems (such as FreeBSD), the following attributes may be present (but may be filled out only when root tries to use them):

 st_gen

File generation number.

On Solaris and derivatives, the following attributes may also be present:

 st_fstype

String that uniquely identifies the type of the filesystem that holds the file.

[Subject index](INDEX.md) · [Previous](os-stat-result-class.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: os.stat_result](os-stat-result-class.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Required continuation of the source contract](stat-macos-and-windows-fields.md)
