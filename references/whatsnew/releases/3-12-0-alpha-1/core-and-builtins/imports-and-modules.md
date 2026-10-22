# Python 3.12.0 alpha 1 / core and builtins / imports and modules

[gh-86298](https://github.com/python/cpython/issues/86298): Whenever `warnings.warn_explicit()` looks to the module's loader, a `DeprecationWarning` fires if `m.__loader__` does not match `m.__spec__.loader`.

[gh-94485](https://github.com/python/cpython/issues/94485): A module's `RESUME` instruction now carries line number 0, matching what [**PEP 626**](https://peps.python.org/pep-0626/) requires.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
