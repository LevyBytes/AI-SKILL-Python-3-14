# Python 3.14.4 final / core and builtins / numeric behavior

[gh-145376](https://github.com/python/cpython/issues/145376): Corrects reference leaks across a number of uncommon error scenarios.

[gh-144759](https://github.com/python/cpython/issues/144759): Corrects undefined behavior inside the lexer whenever the `start` and `multi_line_start` pointers come through as `NULL` within `_PyLexer_remember_fstring_buffers()` plus `_PyLexer_restore_fstring_buffers()`. That `NULL` pointer arithmetic (`NULL - valid_pointer`) is now protected behind explicit `NULL` checks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
