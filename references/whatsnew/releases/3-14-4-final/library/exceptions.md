# Python 3.14.4 final / library / exceptions

[gh-139933](https://github.com/python/cpython/issues/139933): For classes whose custom [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__) method hands back a list of unsortable values, the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) suggestions are now better. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
