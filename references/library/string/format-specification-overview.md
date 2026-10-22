# string — Format specification mini-language — Section introduction and initial examples

### Format specification mini-language

“Format specifications” live inside replacement fields held within a format string and govern how separate values get displayed (see Format string syntax, [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), and [t-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings)). They may likewise be supplied straight to the built-in [`format()`](https://docs.python.org/3.14/library/functions.html#format) function. Every formattable type can decide for itself how the format specification gets read.

The options for format specifications listed here are implemented by most built-in types, though a number of those formatting options apply only to the numeric types.

By common convention, an empty format specification yields the same outcome as calling [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) on the value would. A format specification that is non-empty usually alters the outcome.

A *standard format specifier* takes this general form:

```text

format_spec:             [options][width_and_precision][type]
options:                 [[fill]align][sign]["z"]["#"]["0"]
fill:                    <any character>
align:                   "<" | ">" | "=" | "^"
sign:                    "+" | "-" | " "
width_and_precision:     [width_with_grouping][precision_with_grouping]
width_with_grouping:     [width][grouping]
precision_with_grouping: "." [precision][grouping] | "." grouping
width:                   digit+
precision:               digit+
grouping:                "," | "_"
type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                         | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

When a valid *align* value appears, a *fill* character may sit in front of it; that fill can be any character and falls back to a space when left out. You cannot employ a literal curly brace (”`{`” or “`}`”) as the *fill* character in a [formatted string literal](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) or via the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method. A curly brace can nonetheless be slipped in through a nested replacement field. None of this restricts the [`format()`](https://docs.python.org/3.14/library/functions.html#format) function.

Here is what each alignment option means:

| Option | Meaning |
| --- | --- |
| `'<'` | Forces the field to be left-aligned within the available space (this is the default for most objects). |
| `'>'` | Forces the field to be right-aligned within the available space (this is the default for numbers). |
| `'='` | Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types, excluding `complex`. It becomes the default for numbers when ‘0’ immediately precedes the field width. |
| `'^'` | Forces the field to be centered within the available space. |

Note that without a defined minimum field width, the field width always matches the size of the data filling it, so in that situation the alignment option carries no meaning.

Only number types accept the *sign* option, which may take any one of these:

| Option | Meaning |
| --- | --- |
| `'+'` | Indicates that a sign should be used for both positive as well as negative numbers. |
| `'-'` | Indicates that a sign should be used only for negative numbers (this is the default behavior). |
| space | Indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers. |

After rounding to the format precision, the `'z'` option folds negative-zero floating-point values into positive zero. Only floating-point presentation types accept this option.

Changed in version 3.11: Added the `'z'` option (see also [**PEP 682**](https://peps.python.org/pep-0682/)).

By way of the `'#'` option, the conversion switches to its “alternate form.” What that alternate form means varies from type to type. Only integer, float, and complex types accept this option. With integers, whenever binary, octal, or hexadecimal output is in play, the option prepends the matching prefix `'0b'`, `'0o'`, `'0x'`, or `'0X'` to the output value. With float and complex, the alternate form guarantees the conversion result always carries a decimal-point character, even when no digits trail it. Ordinarily, a decimal-point character shows up in such conversions only when a digit comes after it. Beyond that, `'g'` and `'G'` conversions keep their trailing zeros instead of stripping them.

A decimal integer, the *width* sets the minimum total field width, counting every prefix, separator, and other formatting character. When it is left unset, the content dictates the field width.

With no explicit alignment supplied, putting a zero (`'0'`) character ahead of the *width* field switches on sign-aware zero-padding for numeric types, excluding [`complex`](https://docs.python.org/3.14/library/functions.html#complex). That equals a *fill* character of `'0'` paired with an *alignment* type of `'='`.

Changed in version 3.10: Preceding the *width* field by `'0'` no longer affects the default alignment for strings.

A decimal integer, the *precision* states how many digits appear past the decimal point for presentation types `'f'` and `'F'`, or on each side of the decimal point for presentation types `'g'` or `'G'`. With string presentation types the field sets the largest field size — that is, the count of characters drawn from the field content. The *precision* is not allowed for integer presentation types.

Sitting after the *width* and *precision* fields, the *grouping* option names a digit-group separator for, respectively, the integral and fractional parts of a number. It may be one of these:

| Option | Meaning |
| --- | --- |
| `','` | Inserts a comma every 3 digits for integer presentation type `'d'` and floating-point presentation types, excluding `'n'`. For other presentation types, this option is not supported. |
| `'_'` | Inserts an underscore every 3 digits for integer presentation type `'d'` and floating-point presentation types, excluding `'n'`. For integer presentation types `'b'`, `'o'`, `'x'`, and `'X'`, underscores are inserted every 4 digits. For other presentation types, this option is not supported. |

To get a locale-aware separator instead, reach for the `'n'` float presentation type or integer presentation type.

Changed in version 3.1: Added the `','` option (see also [**PEP 378**](https://peps.python.org/pep-0378/)).

Changed in version 3.6: Added the `'_'` option (see also [**PEP 515**](https://peps.python.org/pep-0515/)).

Changed in version 3.14: Support the *grouping* option for the fractional part.

Lastly, the *type* fixes how the data gets displayed.

These are the available string presentation types:

>

[Subject index](INDEX.md) · [Previous](format-string-syntax.md) · [Continue](format-type-meaning-table.md) · [Owning module, declaration or section: string](string-common-string-operations.md)
