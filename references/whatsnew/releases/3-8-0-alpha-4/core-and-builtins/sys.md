# Python 3.8.0 alpha 4 / core and builtins / sys

[bpo-36588](https://bugs.python.org/issue?@action=redirect&bpo=36588): Under AIX, the major version number is dropped from [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform). The value is now consistently `'aix'` rather than one of `'aix3'` .. `'aix7'`. Because the number was baked into earlier Python releases, the advised idiom is to test with `sys.platform.startswith('aix')`. M. Felt provided this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
