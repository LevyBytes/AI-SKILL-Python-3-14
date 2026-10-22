# Formatted String Literals (f-strings)

### Formatted String Literals (f-strings)

Added in version 3.6.

Changed in version 3.7: Within f-string expressions, [`await`](https://docs.python.org/3.14/reference/expressions.html#await) and [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) became usable.

Changed in version 3.8: Added the debug specifier (`=`)

Changed in version 3.12: A great many limits on f-string expressions were lifted. In particular, backslashes, comments, and nested strings became allowed.

An *f-string* (formally a *formatted string literal*) is a string literal carrying an `f` or `F` prefix. A string literal of this kind permits embedding the outcomes of arbitrary Python expressions inside *replacement fields*, which are bounded by curly brackets (`{}`). Every replacement field has to hold an expression, which may optionally be trailed by:

- a *debug specifier* – an equal sign (`=`);

- a *conversion specifier* – `!s`, `!r` or `!a`; and/or

- a *format specifier* prefixed with a colon (`:`).

Consult the [Lexical Analysis section on f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) for the particulars of these fields' syntax.

[Subject index](INDEX.md) · [Previous](str-title-to-str-zfill.md) · [Continue](debug-specifier.md)
