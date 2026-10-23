# Built-in Functions

*class *int(*number=0*, */*)

 *class *int(*string*, */*, *base=10*)

Build and return an integer object out of a number or a string, falling back to `0` when no arguments are supplied.

Examples:

```pycon
>>> int(123.45)
123
>>> int('123')
123
>>> int('   -12_345\n')
-12345
>>> int('FACE', 16)
64206
>>> int('0xface', 0)
64206
>>> int('01110011', base=2)
115

```

When the argument defines [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__), `int(x)` returns `x.__int__()`. When the argument defines [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__), it returns `x.__index__()`. With floating-point numbers, this truncates toward zero.

When the argument isn't a number, or when *base* is supplied, then it has to be a string, [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) instance that represents an integer in radix *base*. The string may optionally carry a leading `+` or `-` (with no space in between), include leading zeros, sit within whitespace, and feature single underscores placed between digits.

A base-n integer string holds digits, each standing for a value from 0 to n-1. The values 0–9 may be written with any Unicode decimal digit. The values 10–35 may be written with `a` to `z` (or `A` to `Z`). By default *base* is 10. Permitted bases are 0 along with 2–36. Base-2, -8, and -16 strings can carry an optional `0b`/`0B`, `0o`/`0O`, or `0x`/`0X` prefix, just as integer literals do in code. With base 0, the string is read much like an [integer literal in code](https://docs.python.org/3.14/reference/lexical_analysis.html#integers), so that the real base turns out to be 2, 8, 10, or 16 depending on the prefix. Base 0 additionally forbids leading zeros: `int('010', 0)` is not legal, whereas `int('010')` and `int('010', 8)` are.

The integer type is covered in [Numeric Types - int, float, complex](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric).

Changed in version 3.4: When *base* is not an `int` instance yet the *base* object provides a [`base.__index__`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method, that method gets invoked to derive an integer for the base. Earlier releases relied on [`base.__int__`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) rather than `base.__index__`.

Changed in version 3.6: Separating digits using underscores, the way code literals do, became permitted.

Changed in version 3.7: The first parameter is now positional-only.

Changed in version 3.8: Falls back to [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) is not defined.

Changed in version 3.11: Caps can be placed on `int` string inputs and on string representations as a safeguard against denial of service attacks. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised once that cap is passed while turning a string into an `int`, or whenever turning an `int` into a string would run past the cap. Consult the [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits) documentation.

Changed in version 3.14: `int()` no longer delegates to the [`__trunc__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__trunc__) method.

[Subject index](INDEX.md) · [Previous](input.md) · [Continue](INDEX.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
