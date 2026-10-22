# Python 3.12.0 alpha 2 / library / re

[gh-98740](https://github.com/python/cpython/issues/98740): Correct an internal fault in the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module that, on very rare occasions, blocked compilation of a regular expression carrying a [conditional expression](https://docs.python.org/3.14/library/re.html#re-conditional-expression) lacking its "else" branch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
