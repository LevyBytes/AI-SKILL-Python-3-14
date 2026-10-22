# Python 3.13.0 beta 1 / library / binascii

[gh-118314](https://github.com/python/cpython/issues/118314): Resolves a corner case in the strict mode of [`binascii.a2b_base64()`](https://docs.python.org/3.14/library/binascii.html#binascii.a2b_base64) where surplus padding went undetected whenever no padding was actually required.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
