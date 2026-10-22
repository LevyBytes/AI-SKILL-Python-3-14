# Python 3.14.0 alpha 1 / core and builtins / decimal

[gh-118750](https://github.com/python/cpython/issues/118750): When the C build of the `decimal` module is present, `int(str)` now leans on it for an asymptotically far faster conversion. That path only kicks in, though, once the string runs past roughly 2 million digits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
