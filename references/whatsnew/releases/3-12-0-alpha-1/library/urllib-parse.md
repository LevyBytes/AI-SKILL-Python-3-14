# Python 3.12.0 alpha 1 / library / urllib parse

[gh-96035](https://github.com/python/cpython/issues/96035): Corrects a bug within [`urllib.parse.urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse) where some port numbers holding whitespace, underscores, plus and minus signs, or non-ASCII digits were wrongly accepted.

[gh-95865](https://github.com/python/cpython/issues/95865): [`urllib.parse.quote_from_bytes()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.quote_from_bytes) becomes faster as a list comprehension is swapped for `map()`.

[gh-95865](https://github.com/python/cpython/issues/95865): Memory consumption of [`urllib.parse.quote_from_bytes()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.quote_from_bytes) on sizable inputs has been lowered.

Dennis Sweeney provided this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
