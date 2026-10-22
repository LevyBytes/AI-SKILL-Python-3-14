# Python 3.8.0 alpha 1 / library / exceptions

[bpo-22602](https://bugs.python.org/issue?@action=redirect&bpo=22602): For ill-formed sequences opening with "+" (per RFC 2152), the UTF-7 decoder now raises [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError). Zackery Spytz wrote the patch.

[bpo-33217](https://bugs.python.org/issue?@action=redirect&bpo=33217): Raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) on lookups of non-Enum objects within Enum classes and Enum members.

[bpo-35424](https://bugs.python.org/issue?@action=redirect&bpo=35424): The `multiprocessing.Pool` destructor now raises [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) whenever the pool remains running.

[bpo-10496](https://bugs.python.org/issue?@action=redirect&bpo=10496): The `check_environ()` helper in `distutils.utils` now traps [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) when calling [`pwd.getpwuid()`](https://docs.python.org/3.14/library/pwd.html#pwd.getpwuid): under that condition it skips creating the `HOME` environment variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
