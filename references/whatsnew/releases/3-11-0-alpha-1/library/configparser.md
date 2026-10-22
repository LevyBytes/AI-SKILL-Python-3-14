# Python 3.11.0 alpha 1 / library / configparser

[bpo-38741](https://bugs.python.org/issue?@action=redirect&bpo=38741): [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser): a ‘]’ placed within a section header will no longer truncate the section name at that ‘]’

[bpo-45173](https://bugs.python.org/issue?@action=redirect&bpo=45173): Dropped from the [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) module the `SafeConfigParser` class, the `filename` property belonging to [`ParsingError`](https://docs.python.org/3.14/library/configparser.html#configparser.ParsingError), and the `readfp()` method on [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) ? all deprecated as far back as Python 3.2.

Hugo van Kemenade supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
