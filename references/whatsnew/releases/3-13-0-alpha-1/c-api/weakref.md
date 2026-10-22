# Python 3.13.0 alpha 1 / c api / weakref

[gh-105927](https://github.com/python/cpython/issues/105927): The [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) and [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT) functions are deprecated; rely on the new [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) function in their place. Victor Stinner wrote the patch.

[gh-105927](https://github.com/python/cpython/issues/105927): The new [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) function resembles [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) but hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), or `NULL` once the referent is no longer live. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
