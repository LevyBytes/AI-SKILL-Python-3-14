# `printf`-style String Formatting - Section introduction and initial examples

Supplying the equals sign `'='` within an interpolation expression causes the expression's source text to be tacked onto the literal string sitting just before that interpolation. The equals sign itself plus whatever whitespace surrounds it are carried along too. An `Interpolation` instance gets built for the expression in the usual manner, with one change: its [`conversion`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation.conversion) defaults to "`r`" ([`repr()`](https://docs.python.org/3.14/library/functions.html#repr)). Supplying an explicit conversion or format specifier supersedes that default.

### `printf`-style String Formatting

Note

The formatting machinery covered in this section has assorted oddities that produce several frequent mistakes (for instance, not rendering tuples and dictionaries the way you expect).

You can sidestep many of those mistakes by reaching for [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), the `str.format()` interface, or [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template). Every one of these options carries its own mix of simplicity, flexibility, and/or extensibility.

There's a single built-in operation that only `str` objects have: the `%` operator (modulo), which doubles as the string *formatting* or *interpolation* operator. With `format % values` (where *format* is a string), each `%` conversion specification inside *format* gets swapped out for zero or more entries drawn from *values*. This behaves much like calling the `sprintf()` function in C. As an illustration:

```pycon
>>> print('%s has %d quote types.' % ('Python', 2))
Python has 2 quote types.

```

When *format* needs only one argument, *values* can be supplied as a lone non-tuple object. [5] In every other case, *values* has to be a tuple holding precisely as many items as the format string declares, or else a single mapping object (a dictionary, say).

Every conversion specifier holds two or more characters, made up of the following pieces, which have to appear in this sequence:

1.

The `'%'` character, which signals where the specifier begins.

2.

Mapping key (optional), made of a parenthesised run of characters (such as `(somename)`).

3.

Conversion flags (optional), which alter the outcome of certain conversion types.

4.

Minimum field width (optional). When written as an `'*'` (asterisk), the real width is pulled from the next item of the tuple within *values*, and the object being converted follows the minimum field width together with any optional precision.

5.

Precision (optional), written as a `'.'` (dot) trailed by the precision. When given as `'*'` (an asterisk), the real precision is pulled from the next item of the tuple within *values*, and the value being converted comes after the precision.

6.

Length modifier (optional).

7.

Conversion type.

If the right-hand argument is a dictionary (or another mapping type), then every format inside the string *must* carry a parenthesised mapping key into that dictionary placed right after the `'%'` character. That mapping key picks out which value from the mapping should be formatted. As an illustration:

```python
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.

```

Here, a format cannot contain any `*` specifiers (because those depend on a sequential parameter list).

These are the conversion flag characters:

| Flag | Meaning |
| --- | --- |
| `'#'` | The value conversion applies the "alternate form" (as defined further down). |
| `'0'` | For numeric values, the conversion pads with zeros. |
| `'-'` | The result of the conversion is left adjusted (taking priority over the `'0'` conversion should both appear). |
| `' '` | (a space) A space is reserved ahead of a positive number (or an empty string) yielded by a signed conversion. |
| `'+'` | A sign character (`'+'` or `'-'`) leads the conversion (taking priority over a "space" flag). |

You may include a length modifier (`h`, `l`, or `L`), yet Python disregards it because it serves no purpose here — thus, for instance, `%ld` behaves the same as `%d`.

These are the conversion types:

[Subject index](INDEX.md) · [Continue](string-format-conversion-table.md) · [Owning module, declaration or section: Template String Literals (t-strings)](template-string-literals-t-strings.md) · [Preceding source contract and version conditions](template-string-literals-t-strings.md)
