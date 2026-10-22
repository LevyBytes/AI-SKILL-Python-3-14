# Python 3.13.0 alpha 2 / library / compileall

[gh-105931](https://github.com/python/cpython/issues/105931): Adjust [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) so that the stripdir prefix is removed from the full path stored in the compiled `.pyc` file only when that prefix lines up with the very start of the full path completely. Should the prefix not match, nothing is stripped and a warning announcing this is shown.

Formerly, every component of the stripdir prefix that matched the full path got removed, whereas non-matching components were left in place (even those sitting between matching ones).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
