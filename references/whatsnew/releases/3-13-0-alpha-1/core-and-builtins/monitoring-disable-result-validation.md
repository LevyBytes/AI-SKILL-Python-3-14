# Python 3.13.0 alpha 1 / core and builtins / throw valueerror whenever monitoring callback hands back disable events

[gh-106895](https://github.com/python/cpython/issues/106895): Throw a `ValueError` whenever a monitoring callback hands back `DISABLE` for events that lack the ability to be turned off locally.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
