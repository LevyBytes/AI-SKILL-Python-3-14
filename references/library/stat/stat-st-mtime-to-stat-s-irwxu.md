# stat: File timestamps, types and special permission bits

stat.ST_MTIME

Time of last modification.

 stat.ST_CTIME

Whatever the operating system calls the “ctime”. Under Unix-style systems this marks when metadata last changed, while elsewhere — Windows being one case — it marks when the file was created; check your platform's docs for specifics.

What “file size” means depends on the kind of file involved. With ordinary files it is the byte count. With FIFOs and sockets on most Unix variants (Linux among them), it instead reports how many bytes were ready to read when [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`os.fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat), or [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) was invoked — handy at times, particularly when polling such a file after a non-blocking open. For other character and block devices the field's significance is less uniform and hinges on how the relevant system call is implemented.

What follows are the variables that name the flags carried in the `ST_MODE` field.

Reaching for the routines shown earlier travels across platforms better than relying on that first batch of flags:

 stat.S_IFSOCK

Socket.

 stat.S_IFLNK

Symbolic link.

 stat.S_IFREG

Regular file.

 stat.S_IFBLK

Block device.

 stat.S_IFDIR

Directory.

 stat.S_IFCHR

Character device.

 stat.S_IFIFO

FIFO.

 stat.S_IFDOOR

Door.

Added in version 3.4.

 stat.S_IFPORT

Event port.

Added in version 3.4.

 stat.S_IFWHT

Whiteout.

Added in version 3.4.

Note

When a platform lacks support for the relevant file types, `S_IFDOOR`, `S_IFPORT` or `S_IFWHT` each take the value 0.

These flags may likewise be passed in the *mode* argument to [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod):

 stat.S_ISUID

Set UID bit.

 stat.S_ISGID

Set-group-ID bit, which serves more than one purpose. On a directory it signals that BSD rules apply there: any file made inside picks up its group ID from the directory rather than from the effective group ID of whatever process created it, and any subdirectory made there likewise gains the `S_ISGID` bit. On a file whose group execution bit (`S_IXGRP`) is clear, this same bit instead marks mandatory file/record locking (compare `S_ENFMT`).

 stat.S_ISVTX

Sticky bit. Once it is set on a directory, only three parties may rename or delete a file living there: that file's owner, the directory's owner, or a privileged process.

 stat.S_IRWXU

Mask for file owner permissions.

[Subject index](INDEX.md) · [Previous](stat-s-ifmt-to-stat-st-atime.md) · [Continue](stat-s-irusr-to-stat-uf-opaque.md) · [Owning module, declaration or section: stat](stat-s-isdir-to-stat-s-imode.md)
