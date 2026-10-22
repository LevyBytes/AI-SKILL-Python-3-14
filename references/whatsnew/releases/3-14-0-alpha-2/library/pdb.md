# Python 3.14.0 alpha 2 / library / pdb

[gh-125884](https://github.com/python/cpython/issues/125884): Repaired the issue for [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) where breakpoints could not be placed on functions carrying certain annotations.

[gh-58956](https://github.com/python/cpython/issues/58956): Repaired a bug within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) where occasionally a breakpoint failed to fire if it had been placed on a function that already sat in the call stack.

[gh-125378](https://github.com/python/cpython/issues/125378): Repaired the bug within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) where, following a multi-line command, a blank line replayed only the first line out of that multi-line command rather than the whole command.

[gh-125600](https://github.com/python/cpython/issues/125600): Surface the stale code warning inside [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) solely while we render source code.

[gh-125115](https://github.com/python/cpython/issues/125115): Repaired a bug within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) where arguments leading with `-` could not reach the debugged script.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
