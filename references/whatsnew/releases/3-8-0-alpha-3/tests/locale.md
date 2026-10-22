# Python 3.8.0 alpha 3 / tests / locale

[bpo-29571](https://bugs.python.org/issue?@action=redirect&bpo=29571): Repair `test_re.test_locale_flag()`: lean on `locale.getpreferredencoding()` rather than `locale.getlocale()` for fetching the locale encoding. For certain locales, `locale.getlocale()` hands back the wrong encoding.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
