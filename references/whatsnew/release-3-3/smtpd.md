# What's New In Python 3.3 / smtpd

### smtpd

The `smtpd` module has picked up support for [**RFC 5321**](https://datatracker.ietf.org/doc/html/rfc5321.html) (extended SMTP) plus [**RFC 1870**](https://datatracker.ietf.org/doc/html/rfc1870.html) (size extension). Following the standard, those extensions switch on only when the client opens the session using an `EHLO` command.

(The first `ELHO` support came from Alberto Trevino, with the size extension handled by Juhana Jauhiainen; Michele Orr?? together with Dan Boswell put considerable further effort into the patch. [bpo-8739](https://bugs.python.org/issue?@action=redirect&bpo=8739))

[Subject index](INDEX.md) · [Previous source section](signal.md) · [Next source section](smtplib.md) · [Release/subject declaration](summary-release-highlights.md)
