# Python 3.12.0 alpha 7 / library / ssl

[gh-100372](https://github.com/python/cpython/issues/100372): When parsing DER, [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_verify_locations) will no longer mistakenly tolerate certain trailing-data situations.

[gh-96931](https://github.com/python/cpython/issues/96931): Correct the wrong values returned by [`ssl.SSLSocket.shared_ciphers()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.shared_ciphers)

[gh-95495](https://github.com/python/cpython/issues/95495): With a build against OpenSSL 3.0, the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module carried a defect that treated unauthenticated EOFs (that is, ones lacking close_notify) as though they were a clean TLS-level EOF. The module now raises [`SSLEOFError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLEOFError), which lines up with how earlier OpenSSL releases behaved. By default the [`options`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.options) attribute on an [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) likewise stops including [`OP_IGNORE_UNEXPECTED_EOF`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_IGNORE_UNEXPECTED_EOF). Set this option if you want the earlier OpenSSL 3.0 behavior back.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
