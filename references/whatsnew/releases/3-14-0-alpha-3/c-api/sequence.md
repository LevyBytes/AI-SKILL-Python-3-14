# Python 3.14.0 alpha 3 / c api / sequence

[gh-127896](https://github.com/python/cpython/issues/127896): [`PySequence_In()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_In), a function that was never documented, is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated); reach for [`PySequence_Contains()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Contains) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
