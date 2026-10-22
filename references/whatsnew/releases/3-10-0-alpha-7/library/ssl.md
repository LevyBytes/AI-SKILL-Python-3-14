# Python 3.10.0 alpha 7 / library / ssl

[bpo-43577](https://bugs.python.org/issue?@action=redirect&bpo=43577): Resolve a deadlock that occurred when a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) debug callback ran alongside [`ssl.SSLContext.sni_callback()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.sni_callback).

[bpo-39342](https://bugs.python.org/issue?@action=redirect&bpo=39342): Surface `X509_V_FLAG_ALLOW_PROXY_CERTS` under the name [`VERIFY_ALLOW_PROXY_CERTS`](https://docs.python.org/3.14/library/ssl.html#ssl.VERIFY_ALLOW_PROXY_CERTS) so proxy certificate validation can run, as described at [https://docs.openssl.org/1.1.1/man7/proxy-certificates/](https://docs.openssl.org/1.1.1/man7/proxy-certificates/).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
