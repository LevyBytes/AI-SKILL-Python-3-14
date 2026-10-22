# Python 3.5.0 alpha 1 / library / urllib request urlopen takes context object sslcontext argument then drives https

[bpo-22366](https://bugs.python.org/issue?@action=redirect&bpo=22366): urllib.request.urlopen now takes a context object (SSLContext) as an argument, which then drives the HTTPS connection. Alex Gaynor supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
