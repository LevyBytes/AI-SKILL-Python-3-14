# Python 3.14.0 alpha 5 / library / base64

[gh-118761](https://github.com/python/cpython/issues/118761): Boost [`base64.b16decode()`](https://docs.python.org/3.14/library/base64.html#base64.b16decode) by as much as tenfold via a more efficient hexadecimal-digit check over the byte-string. Also lower the import cost of [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) by up to six times because [`re`](https://docs.python.org/3.14/library/re.html#module-re) is no longer imported. The patch came from Bénédikt Tran, Chris Markiewicz, and Adam Turner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
