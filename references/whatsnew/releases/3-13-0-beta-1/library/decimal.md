# Python 3.13.0 beta 1 / library / decimal

[gh-118164](https://github.com/python/cpython/issues/118164): The Python rendering of the `decimal` module could seem to stall on fairly small power cases (such as `2**117`) whenever context precision was cranked very high. A new technique now checks for exactly representable results, one that avoids computing `10**precision` (a value that could be far too big to compute).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
