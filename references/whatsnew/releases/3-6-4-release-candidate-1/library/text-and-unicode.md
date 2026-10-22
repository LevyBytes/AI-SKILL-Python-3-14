# Python 3.6.4 release candidate 1 / library / text and unicode

[bpo-31672](https://bugs.python.org/issue?@action=redirect&bpo=31672): `idpattern` in `string.Template` was matching certain non-ASCII characters. It now relies on the `-i` regular expression local flag so that such non-ASCII characters are excluded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
