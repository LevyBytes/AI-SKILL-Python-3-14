# re - Regular Expression Syntax - Contract: For Unicode (str) patterns:

For Unicode (str) patterns:

Matches Unicode word characters; this takes in every Unicode alphanumeric character (in the sense of [`str.isalnum()`](https://docs.python.org/3.14/library/stdtypes.html#str.isalnum)), along with the underscore (`_`).

Matches `[a-zA-Z0-9_]` if the `ASCII` flag is used.

For 8-bit (bytes) patterns:

Matches the characters treated as alphanumeric within the ASCII character set; this comes to `[a-zA-Z0-9_]`. Should the `LOCALE` flag be used, it matches the characters treated as alphanumeric in the current locale plus the underscore.

`\W`

[Subject index](INDEX.md) · [Previous](regex-lookbehind-example.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Regular Expression Syntax](regular-expression-syntax-overview.md) · [Required continuation of the source contract](regular-expression-w-escape.md)
