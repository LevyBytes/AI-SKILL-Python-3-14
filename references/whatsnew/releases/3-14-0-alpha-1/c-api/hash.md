# Python 3.14.0 alpha 1 / c api / hash

[gh-111389](https://github.com/python/cpython/issues/111389): Introduce the [`PyHASH_MULTIPLIER`](https://docs.python.org/3.14/c-api/hash.html#c.PyHASH_MULTIPLIER) constant: the prime multiplier behind string hashing and assorted other hashes. Victor Stinner wrote the patch.

[gh-122854](https://github.com/python/cpython/issues/122854): Introduce [`Py_HashBuffer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashBuffer), which computes and returns a buffer's hash value. Antoine Pitrou and Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
