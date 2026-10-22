# Python 3.12.0 alpha 2 / library / ftplib

[gh-94172](https://github.com/python/cpython/issues/94172): [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib): Drop the `FTP_TLS.ssl_version` class attribute and rely on the *context* parameter in its place. Victor Stinner authored the patch

[gh-94172](https://github.com/python/cpython/issues/94172): Drop the *keyfile* and *certfile* parameters across the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib), [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib), [`poplib`](https://docs.python.org/3.14/library/poplib.html#module-poplib) and [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) modules, along with the *key_file*, *cert_file* and *check_hostname* parameters from the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) module, every one of them deprecated since Python 3.6. Reach for the *context* parameter (or *ssl_context* in the case of `imaplib`) instead. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
