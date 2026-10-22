# Python 3.13.0 beta 1 / library / json

[gh-95382](https://github.com/python/cpython/issues/95382): Boost the speed of [`json.dumps()`](https://docs.python.org/3.14/library/json.html#json.dumps) and [`json.dump()`](https://docs.python.org/3.14/library/json.html#json.dump) whenever the *indent* argument is supplied. Subject to the data, encoding through `json.dumps()` with *indent* can reach 2 to 3 times the prior speed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
