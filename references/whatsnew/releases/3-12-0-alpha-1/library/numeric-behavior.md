# Python 3.12.0 alpha 1 / library / numeric behavior

[gh-92531](https://github.com/python/cpython/issues/92531): The statistics.median_grouped() function now invariably returns a float. Before, it left the input type unchanged for sequences holding a single element.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
