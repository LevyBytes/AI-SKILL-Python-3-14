# Python 3.5.0 alpha 1 / library / smtplib

[bpo-15014](https://bugs.python.org/issue?@action=redirect&bpo=15014): An ?auth? method was added to smtplib to ease the implementation of auth mechanisms, and the login method now uses it internally.

[bpo-17498](https://bugs.python.org/issue?@action=redirect&bpo=17498): Certain SMTP servers cut the connection following some errors, which breaks strict RFC conformance. Rather than dropping the error code when the following RSET goes out, smtplib now hands back that error code and holds off on raising SMTPServerDisconnected until the subsequent command runs.

[bpo-22216](https://bugs.python.org/issue?@action=redirect&bpo=22216): Following a quit, smtplib now clears its internal state far more thoroughly. Earlier, the clearest symptom was a STARTTLS breakdown across a connect/starttls/quit/connect/starttls sequence.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
