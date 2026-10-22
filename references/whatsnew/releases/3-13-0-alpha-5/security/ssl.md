# Python 3.13.0 alpha 5 / security / ssl

[gh-114572](https://github.com/python/cpython/issues/114572): [`ssl.SSLContext.cert_store_stats()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.cert_store_stats) together with [`ssl.SSLContext.get_ca_certs()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.get_ca_certs) now properly lock their access to the certificate store whenever the [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) is being shared by several threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
