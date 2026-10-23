# What’s New In Python 3.5 / smtplib - smtplib

### smtplib

To make rolling your own authentication mechanisms straightforward, a new [`SMTP.auth()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.auth) method has arrived. Milan Oberkirch contributed this (see [bpo-15014](https://bugs.python.org/issue?@action=redirect&bpo=15014)).

An extra debuglevel (2) is now accepted by the [`SMTP.set_debuglevel()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.set_debuglevel) method, switching on timestamps within debug messages. Gavin Chappell and Maciej Szulik landed this (see [bpo-16914](https://bugs.python.org/issue?@action=redirect&bpo=16914)).

[**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html) (SMTPUTF8) is now honored by the [`SMTP.sendmail()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.sendmail) and [`SMTP.send_message()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.send_message) methods alike. Milan Oberkirch and R. David Murray added this (see [bpo-22027](https://bugs.python.org/issue?@action=redirect&bpo=22027)).

[Subject index](INDEX.md) · [Previous source section](smtpd.md) · [Next source section](sndhdr.md) · [Release/subject declaration](summary-release-highlights.md)
