# Python 3.14.0 beta 4 / library / types

[gh-135878](https://github.com/python/cpython/issues/135878): A crash of [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace) on [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) builds was fixed; it occurred when multiple threads invoked its [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method concurrently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
