# Python 3.7.0 alpha 1 / core and builtins / tune pydict newpresized builds correctly sized dict

[bpo-28731](https://bugs.python.org/issue?@action=redirect&bpo=28731): Tune _PyDict_NewPresized() so it builds a correctly sized dict. This makes a dict literal with constant keys up to 30% quicker.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
