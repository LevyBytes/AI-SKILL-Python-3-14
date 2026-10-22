# Python 3.14.1 final / library / warnings

[gh-138010](https://github.com/python/cpython/issues/138010): Corrects a situation where declaring a class with a base that carries the [`@warnings.deprecated`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated) decorator might fail to call the right [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) method under multiple inheritance. Brian Schubert authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
