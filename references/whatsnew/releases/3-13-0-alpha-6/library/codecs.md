# Python 3.13.0 alpha 6 / library / codecs

[gh-63283](https://github.com/python/cpython/issues/63283): Within [`encodings.idna`](https://docs.python.org/3.14/library/codecs.html#module-encodings.idna), the ACE prefix (`xn--`) may now arrive in any capitalization and still be accepted. Pepijn de Vos and Zackery Spytz supplied the patch.

[gh-85287](https://github.com/python/cpython/issues/85287): Make Unicode codecs raise UnicodeEncodeError or UnicodeDecodeError in place of a plain UnicodeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
