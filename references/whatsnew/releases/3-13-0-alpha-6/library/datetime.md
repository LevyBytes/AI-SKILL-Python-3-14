# Python 3.13.0 alpha 6 / library / datetime

[gh-70647](https://github.com/python/cpython/issues/70647): Open the deprecation window for how [`datetime.datetime.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strptime) and [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) presently behave: they always refuse to parse a date string, raising a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), for a day-of-month case such as `strptime("02-29", "%m-%d")` whenever a year is **not** given and the date lands on February 29th. The aim is to keep users from turning up fresh bugs every four years thanks to a natural but mistaken assumption about the API when parsing partial date values.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
