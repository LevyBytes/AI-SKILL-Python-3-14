# Python 3.8.0 alpha 4 / library / collections and iteration

[bpo-36326](https://bugs.python.org/issue?@action=redirect&bpo=36326): inspect.getdoc() is now able to locate docstrings on member objects even when __slots__ is given as a dictionary.

[bpo-36650](https://bugs.python.org/issue?@action=redirect&bpo=36650): The C build of functools.lru_cache() had been counting a call with an empty `**kwargs` dictionary as separate from a call carrying no keywords whatsoever. The returned value stayed correct, yet a surprise cache miss was the consequence.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
