# Python 3.10.0 beta 1 / windows / os

[bpo-35306](https://bugs.python.org/issue?@action=redirect&bpo=35306): Extra arguments were added to the [`os.startfile()`](https://docs.python.org/3.14/library/os.html#os.startfile) function.

[bpo-38822](https://bugs.python.org/issue?@action=redirect&bpo=38822): Repaired [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat), which used to fail on inaccessible directories carrying a trailing slash rather than reverting to the parent directory's metadata. The flaw also reached [`os.path.exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists) and [`os.path.isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir) indirectly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
