# Python 3.14.0 beta 1 / c api / unicode

[gh-128972](https://github.com/python/cpython/issues/128972): When builds are not free-threaded, [`PyASCIIObject`](https://docs.python.org/3.14/c-api/unicode.html#c.PyASCIIObject) has had its memory layout rolled back to align with Python 3.13. (Keep in mind this structure falls outside the stable ABI, so its memory layout is *guaranteed* to stay stable.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
