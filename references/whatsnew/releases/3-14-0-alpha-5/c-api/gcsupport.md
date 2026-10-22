# Python 3.14.0 alpha 5 / c api / gcsupport

[gh-129533](https://github.com/python/cpython/issues/129533): Reworked [`PyGC_Enable()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Enable), [`PyGC_Disable()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Disable) and [`PyGC_IsEnabled()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_IsEnabled) so they rely on an atomic operation, giving thread-safety under the free-threading build. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
