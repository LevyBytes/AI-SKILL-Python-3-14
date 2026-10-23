# What's New In Python 3.13 / ssl - ssl

### ssl

- Default flags on the [`create_default_context()`](https://docs.python.org/3.14/library/ssl.html#ssl.create_default_context) API now carry [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN) alongside [`VERIFY_X509_STRICT`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_STRICT).

Note

A certificate that predates [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html), or one that is malformed, may be turned away by [`VERIFY_X509_STRICT`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_X509_STRICT) even though the OpenSSL layer beneath might otherwise allow it. Turning that off is discouraged, yet remains possible via:

```python
import ssl

ctx = ssl.create_default_context()
ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT

```

(Contributed by William Woodruff in [gh-112389](https://github.com/python/cpython/issues/112389).)

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](statistics.md) · [Release/subject declaration](summary-release-highlights.md)
