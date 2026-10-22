# Python 3.10.0 alpha 4 / core and builtins / text and unicode

[bpo-40521](https://bugs.python.org/issue?@action=redirect&bpo=40521): Made the Unicode dictionary holding interned strings work with subinterpreters. Victor Stinner authored the patch.

[bpo-39465](https://bugs.python.org/issue?@action=redirect&bpo=39465): Made the `_PyUnicode_FromId()` function operate correctly under subinterpreters. Every interpreter now holds its own array of identifier objects (interned strings decoded out of UTF-8). Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
