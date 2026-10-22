# Python 3.14.0 alpha 2 / c api / dict

[gh-125608](https://github.com/python/cpython/issues/125608): Correct a defect whereby dictionary watchers (for example [`PyDict_Watch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Watch)) registered on an object's attribute dictionary ([`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__)) failed to fire once that object's attributes changed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
