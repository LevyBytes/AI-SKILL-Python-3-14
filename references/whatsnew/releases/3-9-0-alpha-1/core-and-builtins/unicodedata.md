# Python 3.9.0 alpha 1 / core and builtins / unicodedata

[bpo-37966](https://bugs.python.org/issue?@action=redirect&bpo=37966): The [`is_normalized()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.is_normalized) implementation runs much faster now on strings that are not normalized, achieved by coding the complete normalization-quick-check algorithm taken from the Unicode standard.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
