# `printf`-style Bytes Formatting - Section introduction and initial examples

### `printf`-style Bytes Formatting

Note

The formatting operations covered here carry an assortment of quirks that give rise to a number of frequent mistakes (such as not rendering tuples and dictionaries the way you expect). When the value being printed might be a tuple or dictionary, wrap it inside a tuple.

Bytes objects (`bytes`/`bytearray`) own one distinctive built-in operation: the `%` operator (modulo). It also goes by the name of the bytes *formatting* or *interpolation* operator. Given `format % values` (in which *format* is a bytes object), the `%` conversion specifications inside *format* are swapped out for zero or more elements drawn from *values*. The result resembles using `sprintf()` from the C language.

When *format* calls for a single argument, *values* may be a lone non-tuple object. [5] Otherwise, *values* has to be a tuple holding exactly as many items as the format bytes object specifies, or one single mapping object (a dictionary, for instance).

A conversion specifier holds two or more characters and is made of the following components, which have to appear in this order:

1.

The `'%'` character, which signals where the specifier begins.

2.

Mapping key (optional), made up of a parenthesised run of characters (for example, `(somename)`).

3.

Conversion flags (optional), which shape the outcome of certain conversion types.

4.

Minimum field width (optional). When given as an `'*'` (asterisk), the real width is taken from the next element of the tuple in *values*, and the object being converted follows the minimum field width and the optional precision.

5.

Precision (optional), written as a `'.'` (dot) followed by the precision. When given as `'*'` (an asterisk), the real precision is taken from the next element of the tuple in *values*, and the value being converted follows the precision.

6.

Length modifier (optional).

7.

Conversion type.

When the right operand is a dictionary (or another mapping type), then the formats inside the bytes object *must* carry a parenthesised mapping key into that dictionary placed right after the `'%'` character. The mapping key picks the value to be formatted out of the mapping. For instance:

```python
>>> print(b'%(language)s has %(number)03d quote types.' %
...       {b'language': b"Python", b"number": 2})
b'Python has 002 quote types.'

```

Here no `*` specifiers may appear in a format (because they call for a sequential parameter list).

The conversion flag characters are:

| Flag | Meaning |
| --- | --- |
| `'#'` | The value conversion adopts the "alternate form" (defined further down). |
| `'0'` | For numeric values, the conversion gets zero padded. |
| `'-'` | The result is aligned to the left (which overrides the `'0'` conversion when both appear). |
| `' '` | (a space) For a signed conversion, leave one blank ahead of a positive number (or empty string). |
| `'+'` | A sign character (`'+'` or `'-'`) goes in front of the conversion (this overrides a "space" flag). |

A length modifier (`h`, `l`, or `L`) is allowed but gets ignored since Python has no need for it - so, for example, `%ld` is the same as `%d`.

The conversion types are:

[Subject index](INDEX.md) · [Previous](bytes-title-to-bytearray-zfill.md) · [Continue](bytes-format-conversion-table.md)
