# What's New In Python 3.9 / smtplib - smtplib

### smtplib

A timeout of zero passed to the [`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) or [`SMTP_SSL`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP_SSL) constructor now causes a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), so a non-blocking socket is not created by accident. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

The [`LMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.LMTP) constructor gained an optional *timeout* parameter. (Contributed by Donghee Na in [bpo-39329](https://bugs.python.org/issue?@action=redirect&bpo=39329).)

[Subject index](INDEX.md) · [Previous source section](signal.md) · [Next source section](socket.md) · [Release/subject declaration](summary-release-highlights.md)
