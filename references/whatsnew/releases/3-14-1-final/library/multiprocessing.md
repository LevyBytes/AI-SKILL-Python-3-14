# Python 3.14.1 final / library / multiprocessing

[gh-98896](https://github.com/python/cpython/issues/98896): Corrects a multiprocessing resource_tracker failure that occurred when colons appeared inside SharedMemory names. Rani Pinchuk authored the patch.

[gh-131788](https://github.com/python/cpython/issues/131788): Render `ResourceTracker.send` belonging to [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) safe for re-entrancy

[gh-140734](https://github.com/python/cpython/issues/140734): [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): an off-by-one mistake while measuring the length of a temporary socket file path is corrected. Bénédikt Tran authored the patch.

[gh-126631](https://github.com/python/cpython/issues/126631): Resolve a [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) `forkserver` defect that stopped `__main__` from being preloaded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
