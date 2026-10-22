# Python 3.14.0 alpha 5 / c api / object

[gh-128509](https://github.com/python/cpython/issues/128509): Introduced [`PyUnstable_IsImmortal()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_IsImmortal) to check whether a given object is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

[gh-128844](https://github.com/python/cpython/issues/128844): Introduced the [`PyUnstable_TryIncRef()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_TryIncRef) and [`PyUnstable_EnableTryIncRef()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_EnableTryIncRef) unstable APIs. They assist with managing unowned references safely across threads, especially under the free threading build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
