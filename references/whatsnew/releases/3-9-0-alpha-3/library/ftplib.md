# Python 3.9.0 alpha 3 / library / ftplib

[bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259): [`FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) and `FTP_TLS` now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the constructor receives a timeout of zero, avoiding the creation of a non-blocking socket. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
