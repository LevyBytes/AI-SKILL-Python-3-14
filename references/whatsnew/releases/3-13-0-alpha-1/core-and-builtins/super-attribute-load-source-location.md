# Python 3.13.0 alpha 1 / core and builtins / source location load instruction precedes load super attr loads super global

[gh-109195](https://github.com/python/cpython/issues/109195): The source location of the `LOAD_*` instruction that precedes a `LOAD_SUPER_ATTR` (which loads the `super` global, or a shadowing variable) was fixed so it spans only the `super` name rather than the parentheses that follow.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
