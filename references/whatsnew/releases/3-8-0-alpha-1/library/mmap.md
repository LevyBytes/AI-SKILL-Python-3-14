# Python 3.8.0 alpha 1 / library / mmap

[bpo-33767](https://bugs.python.org/issue?@action=redirect&bpo=33767): Carrying out the concatenation (`+`) and repetition (`*`) sequence operations on [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) objects now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) in place of [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Patch by Zackery Spytz.

[bpo-2122](https://bugs.python.org/issue?@action=redirect&bpo=2122): On every platform, the [`mmap.flush()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.flush) method now hands back `None` when it succeeds and raises an exception when it errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
