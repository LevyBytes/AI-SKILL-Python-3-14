# Python 3.14.1 final / library / inspect

[gh-137317](https://github.com/python/cpython/issues/137317): [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) now copes correctly with classes whose wrapped `__init__()` or `__new__()` method employs a descriptor. Yongyu Yan provided the contribution.

[gh-137477](https://github.com/python/cpython/issues/137477): Corrects `inspect.getblock()`, [`inspect.getsourcelines()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsourcelines) and [`inspect.getsource()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsource) when applied to generator expressions.

[gh-139783](https://github.com/python/cpython/issues/139783): Corrects [`inspect.getsourcelines()`](https://docs.python.org/3.14/library/inspect.html#inspect.getsourcelines) for the situation where a comment or a blank line trails a decorator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
