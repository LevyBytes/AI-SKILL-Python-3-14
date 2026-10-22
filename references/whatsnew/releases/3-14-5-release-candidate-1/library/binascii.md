# Python 3.14.5 release candidate 1 / library / binascii

[gh-148093](https://github.com/python/cpython/issues/148093): Correct a one-byte out-of-bounds read inside [`binascii.a2b_uu()`](https://docs.python.org/3.14/library/binascii.html#binascii.a2b_uu); it now raises [`binascii.Error`](https://docs.python.org/3.14/library/binascii.html#binascii.Error) rather than reading beyond the buffer's end.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
