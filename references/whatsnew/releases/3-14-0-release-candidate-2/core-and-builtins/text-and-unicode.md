# Python 3.14.0 release candidate 2 / core and builtins / text and unicode

[gh-137314](https://github.com/python/cpython/issues/137314): Repair a regression in which raw f-strings wrongly processed escape sequences inside format specifications. A raw f-string now keeps literal backslashes within the format spec intact, which lines up with how Python 3.11 acted. As an illustration, `rf"{obj:\xFF}"` now correctly produces `'\\xFF'` instead of `'ÿ'`. Pablo Galindo contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
