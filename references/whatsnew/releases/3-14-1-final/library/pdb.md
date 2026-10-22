# Python 3.14.1 final / library / pdb

[gh-59000](https://github.com/python/cpython/issues/59000): Breakpoint resolution in [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) for class methods is corrected for the situation where the module that defines the class has not been imported.

[gh-125115](https://github.com/python/cpython/issues/125115): Reworks the parsing logic of [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) so that positional arguments flow through as one would expect.

[gh-136057](https://github.com/python/cpython/issues/136057): Repaired a defect across [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) and [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) in which `next` plus `step` could not advance past the line whenever that line held a loop.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
