# Python 3.8.0 alpha 4 / library / inspect

[bpo-33291](https://bugs.python.org/issue?@action=redirect&bpo=33291): The inspect helpers isgeneratorfunction, iscoroutinefunction, and isasyncgenfunction no longer raise AttributeError when handed a method wrapping some arbitrary callable; they simply return False.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
