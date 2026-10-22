# Python 3.9.0 alpha 1 / windows / os

[bpo-37549](https://bugs.python.org/issue?@action=redirect&bpo=37549): [`os.dup()`](https://docs.python.org/3.14/library/os.html#os.dup) no longer fails for standard streams on Windows 7.

[bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834): Under Windows, have [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) treat every name surrogate reparse point, while [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) treats the remaining reparse points, as ordinary files.

[bpo-37267](https://bugs.python.org/issue?@action=redirect&bpo=37267): Under Windows, [`os.dup()`](https://docs.python.org/3.14/library/os.html#os.dup) stops producing an inheritable fd while it handles a character file.

[bpo-36634](https://bugs.python.org/issue?@action=redirect&bpo=36634): [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count) now returns active processors rather than maximum processors.

[bpo-38030](https://bugs.python.org/issue?@action=redirect&bpo=38030): Fixes [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) failing for block devices on Windows

[bpo-38020](https://bugs.python.org/issue?@action=redirect&bpo=38020): Heads off a possible crash where [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) runs (or [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) reaches it indirectly) against a file whose link type is unsupported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
