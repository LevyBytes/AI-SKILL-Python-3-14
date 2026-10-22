# Python 3.12.0 alpha 2 / library / text

[gh-93464](https://github.com/python/cpython/issues/93464): `enum.auto()` now fires correctly even when paired with additional assignment values. For instance, `ONE = auto(), 'some text'` now evaluates to `(1, 'some text')`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
