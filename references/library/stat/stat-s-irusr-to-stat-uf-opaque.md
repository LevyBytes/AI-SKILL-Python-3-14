# stat: File permission bits and user-modifiable flags

stat.S_IRUSR

Owner has read permission.

 stat.S_IWUSR

Owner has write permission.

 stat.S_IXUSR

Owner has execute permission.

 stat.S_IRWXG

Mask for group permissions.

 stat.S_IRGRP

Group has read permission.

 stat.S_IWGRP

Group has write permission.

 stat.S_IXGRP

Group has execute permission.

 stat.S_IRWXO

Mask for permissions for others (not in group).

 stat.S_IROTH

Others have read permission.

 stat.S_IWOTH

Others have write permission.

 stat.S_IXOTH

Others have execute permission.

 stat.S_ENFMT

System V file-locking enforcement. It occupies the same bit as `S_ISGID`: locking of files and records is enforced for any file whose group execution bit (`S_IXGRP`) is not set.

 stat.S_IREAD

Unix V7 synonym for `S_IRUSR`.

 stat.S_IWRITE

Unix V7 synonym for `S_IWUSR`.

 stat.S_IEXEC

Unix V7 synonym for `S_IXUSR`.

The flags below are accepted in the *flags* argument to [`os.chflags()`](https://docs.python.org/3.14/library/os.html#os.chflags):

 stat.UF_SETTABLE

All user settable flags.

Added in version 3.13.

 stat.UF_NODUMP

Do not dump the file.

 stat.UF_IMMUTABLE

The file may not be changed.

 stat.UF_APPEND

The file may only be appended to.

 stat.UF_OPAQUE

The directory is opaque when viewed through a union stack.

[Subject index](INDEX.md) · [Previous](stat-st-mtime-to-stat-s-irwxu.md) · [Continue](stat-uf-nounlink-to-stat-sf-firmlink.md) · [Owning module, declaration or section: stat](stat-s-isdir-to-stat-s-imode.md)
