# Python 3.14.3 final / library / multiprocessing

[gh-109263](https://github.com/python/cpython/issues/109263): Launching a process via the spawn context in [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) no longer changes the start method for the whole program.

[gh-143706](https://github.com/python/cpython/issues/143706): The [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) forkserver now sets [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) properly ahead of preloading `__main__`. Earlier, `sys.argv` stayed empty while the main module was imported in forkserver child processes. This addresses a regression that appeared in 3.13.8 and 3.14.1. Aaron Wieczorek root caused it and Thomas Watson provided the test — thanks!

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
