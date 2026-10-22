# Python 3.9.0 alpha 1 / library / purepath division receives anything not str or purepath instance

[bpo-34775](https://bugs.python.org/issue?@action=redirect&bpo=34775): When PurePath division receives anything that is not a str or PurePath instance, it now yields NotImplemented rather than raising a TypeError. Roger Aiudi wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
