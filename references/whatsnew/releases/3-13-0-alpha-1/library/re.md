# Python 3.13.0 alpha 1 / library / re

[gh-56166](https://github.com/python/cpython/issues/56166): Mark passing the optional arguments *maxsplit*, *count*, and *flags* positionally as deprecated in the module-level functions [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split), [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub), and [`re.subn()`](https://docs.python.org/3.14/library/re.html#re.subn). Those should be supplied by keyword only.

[gh-109631](https://github.com/python/cpython/issues/109631): [`re`](https://docs.python.org/3.14/library/re.html#module-re) routines like [`re.findall()`](https://docs.python.org/3.14/library/re.html#re.findall), [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split), [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search), and [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub), when carrying out short repeated matches, can henceforth be interrupted by the user.

[gh-106052](https://github.com/python/cpython/issues/106052): [`re`](https://docs.python.org/3.14/library/re.html#module-re) module: correct how possessive quantifiers match where a subpattern carries backtracking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
