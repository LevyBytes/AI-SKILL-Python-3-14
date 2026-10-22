# Python 3.14.0 beta 1 / library / inspect

[gh-119605](https://github.com/python/cpython/issues/119605): Honor `follow_wrapped` for the `__init__()` and `__new__()` methods while obtaining a class signature for a class through [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature). Keep the class signature intact after it is wrapped with [`warnings.deprecated()`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated). Patch by Xuehai Pan.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
