# Python 3.13.0 alpha 6 / library / functions

[gh-109870](https://github.com/python/cpython/issues/109870): Dataclasses now invoke [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) a single time per dataclass rather than once for each method it adds. Building a dataclass can therefore become as much as 20% quicker.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
