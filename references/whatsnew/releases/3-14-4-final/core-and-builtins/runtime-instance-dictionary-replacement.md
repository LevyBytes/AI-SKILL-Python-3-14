# Python 3.14.4 final / core and builtins / corrects mistaken clearing object s dict whenever gets overwritten

[gh-130327](https://github.com/python/cpython/issues/130327): Corrects mistaken clearing of an object's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) whenever it gets overwritten at runtime.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
