# Python 3.14.0 alpha 5 / core and builtins / codecs

[gh-126004](https://github.com/python/cpython/issues/126004): Corrected how the [`codecs.replace_errors()`](https://docs.python.org/3.14/library/codecs.html#codecs.replace_errors) error handler treats the [`UnicodeError.start`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.start) and [`UnicodeError.end`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.end) values. Bénédikt Tran supplied the patch.

[gh-126004](https://github.com/python/cpython/issues/126004): Corrected how the [`codecs.backslashreplace_errors()`](https://docs.python.org/3.14/library/codecs.html#codecs.backslashreplace_errors) error handler treats the [`UnicodeError.start`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.start) and [`UnicodeError.end`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.end) values. Bénédikt Tran supplied the patch.

[gh-126004](https://github.com/python/cpython/issues/126004): Corrected how the [`codecs.xmlcharrefreplace_errors()`](https://docs.python.org/3.14/library/codecs.html#codecs.xmlcharrefreplace_errors) error handler treats the [`UnicodeError.start`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.start) and [`UnicodeError.end`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.end) values. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
