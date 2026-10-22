# Python 3.14.0 alpha 5 / c api / sequence

[gh-91417](https://github.com/python/cpython/issues/91417): Dropped [`PySequence_Fast()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast) from the limited C API, because pairing it with [`PySequence_Fast_GET_ITEM`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Fast_GET_ITEM) was required yet that helper never functioned in the limited C API. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
