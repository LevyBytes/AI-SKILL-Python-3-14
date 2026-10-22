# Python 3.6.0 beta 1 / core and builtins / text and unicode

[bpo-27948](https://bugs.python.org/issue?@action=redirect&bpo=27948): Inside f-strings, backslashes are now permitted only within the braces (the part that holds the expressions). Relative to the 3.6 alpha releases — where a backslash could sit anywhere in an f-string — this breaks compatibility. Expressions in f-strings must also be wrapped in literal braces rather than escapes such as `f'\x7b"hi"\x7d'`.

[bpo-27364](https://bugs.python.org/issue?@action=redirect&bpo=27364): A backslash-character pairing that isn’t a valid escape sequence now produces a DeprecationWarning. Emanuel Barry wrote the patch.

[bpo-27078](https://bugs.python.org/issue?@action=redirect&bpo=27078): A BUILD_STRING opcode was added. f-strings evaluation was optimized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
