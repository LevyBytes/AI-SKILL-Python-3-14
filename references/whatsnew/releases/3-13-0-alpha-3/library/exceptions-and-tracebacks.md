# Python 3.13.0 alpha 3 / library / exceptions and tracebacks

[gh-113358](https://github.com/python/cpython/issues/113358): Resolved rendering of tracebacks for exceptions carrying a broken __getattr__

[gh-113149](https://github.com/python/cpython/issues/113149): Sharpened the error message thrown when a JSON array or object holds a trailing comma. Carson Radtke supplied this patch.

[gh-112540](https://github.com/python/cpython/issues/112540): Whenever a dataset includes a zero, the statistics.geometric_mean() function now hands back zero. Earlier it would raise an exception instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
