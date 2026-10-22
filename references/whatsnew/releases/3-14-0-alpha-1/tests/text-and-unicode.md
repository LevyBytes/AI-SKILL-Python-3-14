# Python 3.14.0 alpha 1 / tests / text and unicode

[gh-121188](https://github.com/python/cpython/issues/121188): While building the JUnit XML file, regrtest now escapes characters that XML forbids, for instance the chr(27) control character that appears in ANSI escape sequences. Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
