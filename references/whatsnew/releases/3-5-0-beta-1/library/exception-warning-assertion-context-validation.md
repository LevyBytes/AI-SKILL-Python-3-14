# Python 3.5.0 beta 1 / library / context manager mode assertraises assertraisesregex assertwarns assertwarnsregex checks raise

[bpo-24134](https://bugs.python.org/issue?@action=redirect&bpo=24134): In context manager mode, assertRaises(), assertRaisesRegex(), assertWarns() and assertWarnsRegex() checks now raise a deprecation warning whenever callable is None or keyword arguments other than msg are supplied.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
