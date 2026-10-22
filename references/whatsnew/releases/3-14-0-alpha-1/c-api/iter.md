# Python 3.14.0 alpha 1 / c api / iter

[gh-105201](https://github.com/python/cpython/issues/105201): Introduce [`PyIter_NextItem()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_NextItem) as a stand-in for [`PyIter_Next()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Next), whose return value is ambiguous. Irit Katriel and Erlend Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
