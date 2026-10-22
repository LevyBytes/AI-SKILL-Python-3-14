# Python 3.6.6 release candidate 1 / library / empty sequences random random choice reliably raises indexerror even invoked subclasses

[bpo-33203](https://bugs.python.org/issue?@action=redirect&bpo=33203): For empty sequences, `random.Random.choice()` now reliably raises `IndexError`, even when invoked from subclasses lacking a `getrandbits()` implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
