# Python 3.11.0 alpha 1 / tests / ssl

[bpo-43921](https://bugs.python.org/issue?@action=redirect&bpo=43921): Repair test_ssl.test_wrong_cert_tls13() by passing `suppress_ragged_eofs=False`, because on Windows a call to `read()` may surface [`ssl.SSLEOFError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLEOFError). Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
