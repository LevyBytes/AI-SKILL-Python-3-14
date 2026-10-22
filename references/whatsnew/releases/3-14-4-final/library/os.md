# Python 3.14.4 final / library / os

[gh-143698](https://github.com/python/cpython/issues/143698): When the *scheduler* passed to [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) or [`os.posix_spawnp()`](https://docs.python.org/3.14/library/os.html#os.posix_spawnp) isn't a tuple, the code now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
