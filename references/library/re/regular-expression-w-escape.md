# re — Regular-expression \W escape

Matches every character that does not count as a word character, making it the inverse of `\w`. Without extra flags, it matches any non-underscore (`_`) character for which [`str.isalnum()`](https://docs.python.org/3.14/library/stdtypes.html#str.isalnum) yields `False`.

With the `ASCII` flag in effect, it matches `[^a-zA-Z0-9_]`.

When the `LOCALE` flag is active, it matches each character that is neither the underscore nor alphanumeric according to the active locale.

[Subject index](INDEX.md) · [Continue](regular-expression-syntax.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Regular-expression \W escape](regular-expression-syntax-contract-for-unicode-str-patterns.md) · [Preceding source contract and version conditions](regular-expression-syntax-contract-for-unicode-str-patterns.md)
