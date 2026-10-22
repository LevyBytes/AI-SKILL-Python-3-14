# Python 3.13.0 alpha 4 / c api / list

[gh-114329](https://github.com/python/cpython/issues/114329): Introduced [`PyList_GetItemRef()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItemRef), comparable to [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem) except that it yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) rather than a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
