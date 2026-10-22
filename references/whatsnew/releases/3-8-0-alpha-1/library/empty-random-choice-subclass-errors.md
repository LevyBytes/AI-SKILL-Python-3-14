# Python 3.8.0 alpha 1 / library / random random choice consistently raises indexerror empty sequences even invoked subclasses

[bpo-33203](https://bugs.python.org/issue?@action=redirect&bpo=33203): `random.Random.choice()` now consistently raises `IndexError` for empty sequences, even when invoked from subclasses lacking a `getrandbits()` implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
