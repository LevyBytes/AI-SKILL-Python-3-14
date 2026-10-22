# Python 3.14.5 release candidate 1 / library / smtplib

[gh-70039](https://github.com/python/cpython/issues/70039): Repaired a defect where [`smtplib.SMTP.starttls()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.starttls) might break if [`smtplib.SMTP.connect()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.connect) had been invoked explicitly instead of implicitly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
