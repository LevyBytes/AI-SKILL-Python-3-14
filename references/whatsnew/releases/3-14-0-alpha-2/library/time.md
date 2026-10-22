# Python 3.14.0 alpha 2 / library / time

[gh-52551](https://github.com/python/cpython/issues/52551): Rely on `wcsftime()` to build [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) under Windows.

[gh-52551](https://github.com/python/cpython/issues/52551): Repair encoding problems inside [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime), the [`strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) method belonging to the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) classes [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time), plus how those classes format. Characters the current locale cannot encode are now allowed within the format string. Surrogate pairs together with sequences of surrogatescape-encoded bytes no longer get recombinated. An embedded null character no longer cuts the format string short.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
