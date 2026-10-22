# Python 3.13.0 alpha 1 / c api / dict

[gh-106004](https://github.com/python/cpython/issues/106004): The [`PyDict_GetItemRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemRef) and [`PyDict_GetItemStringRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemStringRef) functions are added; they parallel [`PyDict_GetItemWithError()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemWithError) yet give back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) in place of a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). Victor Stinner wrote the patch.

[gh-108314](https://github.com/python/cpython/issues/108314): The new [`PyDict_ContainsString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_ContainsString) function matches [`PyDict_Contains()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Contains), except that *key* is given as a const char* UTF-8 encoded bytes string instead of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
