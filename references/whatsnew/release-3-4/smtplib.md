# What's New In Python 3.4 / smtplib — smtplib

### smtplib

[`SMTPException`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTPException) now descends from [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), so that both socket-level failures and SMTP-protocol-level failures can be trapped within a single try/except block by code whose only concern is whether something went wrong. (Contributed by Ned Jackson Lovely in [bpo-2118](https://bugs.python.org/issue?@action=redirect&bpo=2118).)

[Subject index](INDEX.md) · [Previous source section](smtpd.md) · [Next source section](socket.md) · [Release/subject declaration](release-highlights.md)
