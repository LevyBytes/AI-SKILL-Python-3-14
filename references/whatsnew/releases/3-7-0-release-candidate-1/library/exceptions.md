# Python 3.7.0 release candidate 1 / library / exceptions

[bpo-33767](https://bugs.python.org/issue?@action=redirect&bpo=33767): Both concatenation (`+`) and repetition (`*`) on sequences now raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) when applied to [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) objects. Patch by Zackery Spytz.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
