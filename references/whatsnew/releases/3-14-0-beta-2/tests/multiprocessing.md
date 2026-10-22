# Python 3.14.0 beta 2 / tests / multiprocessing

[gh-133744](https://github.com/python/cpython/issues/133744): Repair the multiprocessing interrupt test. An event was added to coordinate the parent with the child process: it holds until the child begins sleeping. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
