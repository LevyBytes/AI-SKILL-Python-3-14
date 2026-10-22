# Python 3.14.0 release candidate 3 / library / smtplib

[gh-136134](https://github.com/python/cpython/issues/136134): When Python was compiled lacking MD5 support, `SMTP.auth_cram_md5()` now throws an [`SMTPException`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTPException) rather than a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Notably, an [`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) client refrains from invoking this method even when the remote server is presumed to allow it. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
