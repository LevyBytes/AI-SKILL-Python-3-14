# Python 3.14.0 alpha 6 / library / unicodedata

[gh-129569](https://github.com/python/cpython/issues/129569): Fixes [`unicodedata.normalize()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize) so it consistently hands back a built-in [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object when fed a `str` subclass, no matter whether that string was already normalized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
