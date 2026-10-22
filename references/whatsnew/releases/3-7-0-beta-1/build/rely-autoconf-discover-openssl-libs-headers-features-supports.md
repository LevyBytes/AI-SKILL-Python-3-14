# Python 3.7.0 beta 1 / build / rely autoconf discover openssl libs headers features supports

[bpo-32598](https://bugs.python.org/issue?@action=redirect&bpo=32598): Rely on autoconf to discover OpenSSL libs, headers and the features it supports. To find OpenSSL the ax_check_openssl M4 macro turns to pkg-config, dropping back to a manual search.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
