# What's New In Python 3.3 / ftplib - ftplib

### ftplib

- A `source_address` keyword argument now reaches [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP); it names the `(host, port)` to bind as the source while the outgoing socket is opened. Giampaolo Rodolà landed this ([bpo-8594](https://bugs.python.org/issue?@action=redirect&bpo=8594)).

- A fresh [`ccc()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS.ccc) function on the [`FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) class drops the control channel back to plaintext. That helps when you want firewalls that handle NAT for non-secure FTP to work without you opening fixed ports. Giampaolo Rodolà landed this ([bpo-12139](https://bugs.python.org/issue?@action=redirect&bpo=12139)).

- A new [`ftplib.FTP.mlsd()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.mlsd) method delivers a directory listing in a parsable form and marks both [`ftplib.FTP.nlst()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.nlst) and [`ftplib.FTP.dir()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.dir) deprecated. Giampaolo Rodolà landed this ([bpo-11072](https://bugs.python.org/issue?@action=redirect&bpo=11072)).

[Subject index](INDEX.md) · [Previous source section](email-other-api-changes.md) · [Next source section](functools.md) · [Release/subject declaration](summary-release-highlights.md)
