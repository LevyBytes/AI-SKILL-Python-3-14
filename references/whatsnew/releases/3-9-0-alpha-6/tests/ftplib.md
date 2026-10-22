# Python 3.9.0 alpha 6 / tests / ftplib

[bpo-39380](https://bugs.python.org/issue?@action=redirect&bpo=39380): The encoding argument was added to the [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) and [`ftplib.FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) constructors as keyword-only, with its default switched from `latin-1` over to `utf-8` so as to honor [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
