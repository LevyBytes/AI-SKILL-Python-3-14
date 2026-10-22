# Python 3.14.0 alpha 2 / library / inspect

[gh-70764](https://github.com/python/cpython/issues/70764): Repaired a situation where [`inspect.getclosurevars()`](https://docs.python.org/3.14/library/inspect.html#inspect.getclosurevars) wrongly labelled an attribute name as a global variable when that name shows up both as an attribute name and as a global variable.

[gh-125633](https://github.com/python/cpython/issues/125633): Introduce the [`inspect.ispackage()`](https://docs.python.org/3.14/library/inspect.html#inspect.ispackage) function for deciding whether some object is a [package](https://docs.python.org/3.14/glossary.html#term-package) or not.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
