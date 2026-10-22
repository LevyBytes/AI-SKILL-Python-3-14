# Python 3.9.0 alpha 3 / library / smtplib

[bpo-39329](https://bugs.python.org/issue?@action=redirect&bpo=39329): An optional *timeout* parameter was added to the [`LMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.LMTP) constructor. Donghee Na wrote the patch.

[bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259): [`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) and [`SMTP_SSL`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP_SSL) now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the constructor receives a timeout of zero, avoiding the creation of a non-blocking socket. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
