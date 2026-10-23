# What's New In Python 3.3 / smtplib - smtplib

### smtplib

The [`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP), [`SMTP_SSL`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP_SSL), and [`LMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.LMTP) classes now take a `source_address` keyword argument that names the `(host, port)` to bind as the source address when the outgoing socket is opened. (Contributed by Paulo Scardine in [bpo-11281](https://bugs.python.org/issue?@action=redirect&bpo=11281).)

[`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) now honors the context management protocol, so an `SMTP` instance can drive a `with` statement. (Contributed by Giampaolo Rodol?? in [bpo-11289](https://bugs.python.org/issue?@action=redirect&bpo=11289).)

Both the [`SMTP_SSL`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP_SSL) constructor and the [`starttls()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.starttls) method now take an SSLContext parameter for tuning the secure channel's settings. (Contributed by Kasun Herath in [bpo-8809](https://bugs.python.org/issue?@action=redirect&bpo=8809).)

[Subject index](INDEX.md) · [Previous source section](smtpd.md) · [Next source section](socket.md) · [Release/subject declaration](summary-release-highlights.md)
