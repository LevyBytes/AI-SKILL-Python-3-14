# Python 3.5.4 release candidate 1 / tests / locale

[bpo-29571](https://bugs.python.org/issue?@action=redirect&bpo=29571): so its behaviour lines up with the `re.LOCALE` flag, test_re.test_locale_flag now calls `locale.getpreferredencoding(False)` to pick the encoding it tries for the test regex, which lets the test be skipped properly whenever the default locale encoding happens to be multi-byte

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
