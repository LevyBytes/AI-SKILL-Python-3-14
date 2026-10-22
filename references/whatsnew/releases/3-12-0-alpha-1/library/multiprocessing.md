# Python 3.12.0 alpha 1 / library / multiprocessing

[gh-90549](https://github.com/python/cpython/issues/90549): Repair a multiprocessing defect in which a globally named resource (a semaphore, say) might leak whenever a child process was spawned rather than forked.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
