# Python 3.7.0 alpha 2 / library / text and unicode

[bpo-31672](https://bugs.python.org/issue?@action=redirect&bpo=31672): The `idpattern` in `string.Template` had been matching certain non-ASCII characters. It now applies the `-i` regular expression local flag so non-ASCII characters are excluded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
