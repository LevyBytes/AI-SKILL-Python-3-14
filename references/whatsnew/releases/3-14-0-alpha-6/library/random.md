# Python 3.14.0 alpha 6 / library / random

[gh-130285](https://github.com/python/cpython/issues/130285): Repairs an edge case in [`random.sample()`](https://docs.python.org/3.14/library/random.html#random.sample) that lets the *counts* parameter describe an empty population. As a result, `sample([], 0, counts=[])` and `sample('abc', k=0, counts=[0, 0, 0])` now both yield what `sample([], 0)` returns.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
