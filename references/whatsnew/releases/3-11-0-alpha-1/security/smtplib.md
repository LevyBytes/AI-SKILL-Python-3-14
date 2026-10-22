# Python 3.11.0 alpha 1 / security / smtplib

[bpo-43124](https://bugs.python.org/issue?@action=redirect&bpo=43124): Adjusted the internal `putcmd` routine in [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) so it scrubs input for any `\r` and `\n` characters, guarding against the (improbable) command injection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
