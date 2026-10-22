# Python 3.13.0 alpha 1 / security / ssl

[gh-108310](https://github.com/python/cpython/issues/108310): A flaw was corrected in which [`ssl.SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) instances could be tricked into skipping the TLS handshake and its safeguards (certificate verification among them), then treating unencrypted bytes that were sent as though they were post-handshake TLS-encrypted data. Aapo Oksman filed the security report as [**CVE 2023-40217**](https://www.cve.org/CVERecord?id=CVE-2023-40217); Gregory P. Smith wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
