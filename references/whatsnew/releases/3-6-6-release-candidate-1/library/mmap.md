# Python 3.6.6 release candidate 1 / library / mmap

[bpo-33767](https://bugs.python.org/issue?@action=redirect&bpo=33767): On [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) objects, the concatenation (`+`) and repetition (`*`) sequence operations now throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Zackery Spytz contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
