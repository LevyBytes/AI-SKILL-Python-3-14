# Python 3.14.6 final / security / unicodedata

[gh-149079](https://github.com/python/cpython/issues/149079): Repair a possible denial of service within [`unicodedata.normalize()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize). To reorder combining characters, the canonical ordering phase of Unicode normalization relied on a quadratic-time insertion sort, which a crafted payload bearing many combining characters out of canonical order could abuse. That step now uses a linear-time counting sort across long runs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
