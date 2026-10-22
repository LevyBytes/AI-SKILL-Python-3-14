# os — Files and Directories — Signature and initial contract

os.chmod(*path*, *mode*, ***, *dir_fd=None*, *follow_symlinks=True*)

Switch the mode of *path* over to the numeric *mode*. For *mode* you may pass any one of the values below (declared within the [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module) or bitwise ORed combinations thereof:

- [`stat.S_ISUID`](https://docs.python.org/3.14/library/stat.html#stat.S_ISUID)

- [`stat.S_ISGID`](https://docs.python.org/3.14/library/stat.html#stat.S_ISGID)

- [`stat.S_ENFMT`](https://docs.python.org/3.14/library/stat.html#stat.S_ENFMT)

- [`stat.S_ISVTX`](https://docs.python.org/3.14/library/stat.html#stat.S_ISVTX)

- [`stat.S_IREAD`](https://docs.python.org/3.14/library/stat.html#stat.S_IREAD)

- [`stat.S_IWRITE`](https://docs.python.org/3.14/library/stat.html#stat.S_IWRITE)

- [`stat.S_IEXEC`](https://docs.python.org/3.14/library/stat.html#stat.S_IEXEC)

- [`stat.S_IRWXU`](https://docs.python.org/3.14/library/stat.html#stat.S_IRWXU)

- [`stat.S_IRUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IRUSR)

- [`stat.S_IWUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IWUSR)

- [`stat.S_IXUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IXUSR)

- [`stat.S_IRWXG`](https://docs.python.org/3.14/library/stat.html#stat.S_IRWXG)

- [`stat.S_IRGRP`](https://docs.python.org/3.14/library/stat.html#stat.S_IRGRP)

- [`stat.S_IWGRP`](https://docs.python.org/3.14/library/stat.html#stat.S_IWGRP)

- [`stat.S_IXGRP`](https://docs.python.org/3.14/library/stat.html#stat.S_IXGRP)

- [`stat.S_IRWXO`](https://docs.python.org/3.14/library/stat.html#stat.S_IRWXO)

- [`stat.S_IROTH`](https://docs.python.org/3.14/library/stat.html#stat.S_IROTH)

- [`stat.S_IWOTH`](https://docs.python.org/3.14/library/stat.html#stat.S_IWOTH)

- [`stat.S_IXOTH`](https://docs.python.org/3.14/library/stat.html#stat.S_IXOTH)

Support is available here for giving a file descriptor, for paths relative to directory descriptors, and for skipping symlink resolution.

Note

[Subject index](INDEX.md) · [Previous](os-chflags-to-stat-sf-snapshot.md) · [Continue](chmod-windows-permission-limits.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
