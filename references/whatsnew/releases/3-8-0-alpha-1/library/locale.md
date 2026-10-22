# Python 3.8.0 alpha 1 / library / locale

[bpo-28604](https://bugs.python.org/issue?@action=redirect&bpo=28604): [`locale.localeconv()`](https://docs.python.org/3.14/library/locale.html#locale.localeconv) now switches the `LC_CTYPE` locale temporarily over to the `LC_MONETARY` locale whenever those two locales differ and the monetary strings contain non-ASCII characters. That temporary switch affects other threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
