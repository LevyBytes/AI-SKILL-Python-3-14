# Python 3.12.0 alpha 1 / library / platform

[gh-93033](https://github.com/python/cpython/issues/93033): Searching within certain strings is now as much as 10 times quicker; the affected range varies by platform — Windows covers [U+0xFFFF, U+0x0100], while 64-bit Linux covers [U+0xFFFFFFFF, U+0x00010000].

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
