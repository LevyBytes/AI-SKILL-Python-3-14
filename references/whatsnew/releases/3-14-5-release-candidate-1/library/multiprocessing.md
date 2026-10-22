# Python 3.14.5 release candidate 1 / library / multiprocessing

[gh-146313](https://github.com/python/cpython/issues/146313): Clear a deadlock inside the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) resource tracker, where during interpreter shutdown the parent could stall forever in [`os.waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid) if a child spawned through [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) was still keeping the tracker's pipe open.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
