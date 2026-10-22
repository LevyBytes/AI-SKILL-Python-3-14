# Python 3.7.0 alpha 1 / library / hostname checking certificate requirement

[bpo-31431](https://bugs.python.org/issue?@action=redirect&bpo=31431): SSLContext.check_hostname now sets SSLContext.verify_mode to ssl.CERT_REQUIRED on its own rather than raising a ValueError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
