# Python 3.6.1 release candidate 1 / tests / locale

[bpo-29571](https://bugs.python.org/issue?@action=redirect&bpo=29571): so that it mirrors how the `re.LOCALE` flag behaves, test_re.test_locale_flag now relies on `locale.getpreferredencoding(False)` to figure out the candidate encoding for the test regex (which lets it skip correctly whenever the default locale encoding happens to be multi-byte)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
