# Python 3.13.0 alpha 3 / library / getpass

[bpo-32731](https://bugs.python.org/issue?@action=redirect&bpo=32731): For every failure, [`getpass.getuser()`](https://docs.python.org/3.14/library/getpass.html#getpass.getuser) now raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead of raising [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) on systems without the [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd) module or [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) when the password database holds nothing.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
