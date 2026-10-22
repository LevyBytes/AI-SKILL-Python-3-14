# Python 3.11.0 beta 1 / library / numeric behavior

[gh-91700](https://github.com/python/cpython/issues/91700): Compiling a regular expression that has a conditional expression `(?(group)...)` now raises a fitting `re.error` whenever the group number points at a group that was not defined. An internal RuntimeError was raised in the past.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
