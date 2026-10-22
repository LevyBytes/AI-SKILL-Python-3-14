# Python 3.13.0 alpha 3 / library / os

[gh-113191](https://github.com/python/cpython/issues/113191): On Windows, [`os.fchmod()`](https://docs.python.org/3.14/library/os.html#os.fchmod) is now supported, and [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod) now accepts a file descriptor.

[gh-113119](https://github.com/python/cpython/issues/113119): Passing `env=None` to [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) is now permitted, causing the freshly spawned process to inherit the environment of the current one. Jakub Kulik wrote the patch.

[gh-59616](https://github.com/python/cpython/issues/59616): On Windows, add support for [`os.lchmod()`](https://docs.python.org/3.14/library/os.html#os.lchmod) plus the *follow_symlinks* argument of [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod). Be aware that on Windows `os.lchmod()` defaults *follow_symlinks* to `False`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
