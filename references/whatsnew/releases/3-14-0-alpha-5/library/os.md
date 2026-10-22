# Python 3.14.0 alpha 5 / library / os

[gh-129005](https://github.com/python/cpython/issues/129005): Make `_pyio.FileIO.readinto` faster by dropping needless objects and copies through the use of [`os.readinto()`](https://docs.python.org/3.14/library/os.html#os.readinto).

[gh-129205](https://github.com/python/cpython/issues/129205): Provide [`os.readinto()`](https://docs.python.org/3.14/library/os.html#os.readinto), which reads from a file descriptor straight into a [buffer object](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

[gh-128636](https://github.com/python/cpython/issues/128636): Stop PyREPL from failing whenever [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) gets replaced with an invalid value.

[gh-81340](https://github.com/python/cpython/issues/81340): Adopt [`os.copy_file_range()`](https://docs.python.org/3.14/library/os.html#os.copy_file_range) by default within the [`shutil.copy()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy), [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2), and [`shutil.copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile) functions. The underlying Linux system call lets filesystems opt into copy-on-write (for btrfs and XFS) or server-side copy (for NFS.) Illia Volochii supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
