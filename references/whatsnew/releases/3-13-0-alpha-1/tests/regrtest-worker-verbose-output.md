# Python 3.13.0 alpha 1 / tests / regrtest worker processes jn combined verbose3 option harness can

[gh-110367](https://github.com/python/cpython/issues/110367): regrtest: With worker processes (-jN) combined with the ?verbose3 option, the harness can now surface worker output even when a worker process crashes. Earlier, sys.stdout and sys.stderr got swapped out, so a crash discarded the worker output entirely. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
