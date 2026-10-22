# Python 3.14.0 alpha 5 / library / hashlib

[gh-128657](https://github.com/python/cpython/issues/128657): Repair a possible extra reference left behind by objects that [`hashlib.sha256()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.sha256) returns when running under [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
