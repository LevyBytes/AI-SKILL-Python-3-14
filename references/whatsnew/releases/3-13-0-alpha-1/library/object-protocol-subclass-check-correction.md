# Python 3.13.0 alpha 1 / library / cleared up long standing defect where issubclass object typing protocol resolved

[gh-105239](https://github.com/python/cpython/issues/105239): Cleared up a long-standing defect where `issubclass(object, typing.Protocol)` resolved to `True` in certain corner situations. Alex Waygood authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
