# Python 3.14.1 final / core and builtins / copy

[gh-105487](https://github.com/python/cpython/issues/105487): Strip the nonexistent [`__copy__()`](https://docs.python.org/3.14/library/copy.html#object.__copy__), [`__deepcopy__()`](https://docs.python.org/3.14/library/copy.html#object.__deepcopy__), plus [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) from the [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__) entries belonging to [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
