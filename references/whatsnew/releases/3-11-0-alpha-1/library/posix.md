# Python 3.11.0 alpha 1 / library / posix

[bpo-45012](https://bugs.python.org/issue?@action=redirect&bpo=45012): Within [`posix`](https://docs.python.org/3.14/library/posix.html#module-posix), let go of the GIL across the `stat()`, `lstat()`, and `fstatat()` syscalls that [`os.DirEntry.stat()`](https://docs.python.org/3.14/library/os.html#os.DirEntry.stat) performs. Stanisław Skonieczny contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
