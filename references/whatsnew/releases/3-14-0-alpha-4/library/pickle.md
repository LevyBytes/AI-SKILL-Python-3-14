# Python 3.14.0 alpha 4 / library / pickle

[gh-118761](https://github.com/python/cpython/issues/118761): Cut [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) import time by a quarter through dropping a needless regular expression. Because of that, [`re`](https://docs.python.org/3.14/library/re.html#module-re) is no longer pulled in implicitly as `pickle.re`. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
