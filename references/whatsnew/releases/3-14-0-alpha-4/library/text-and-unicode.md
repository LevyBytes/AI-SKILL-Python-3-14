# Python 3.14.0 alpha 4 / library / text and unicode

[gh-127196](https://github.com/python/cpython/issues/127196): Resolved a crash that struck when a dict bearing keys in an invalid encoding reached several functions of the `_interpreters` module.

[gh-124130](https://github.com/python/cpython/issues/124130): Corrected a defect in matching the regular expression `\B` against an empty input string. It now always mirrors the opposite of `\b`. For the former behavior, write `(?!\A\Z)\B`; for the new behavior on older Python releases, write `(?!\b)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
