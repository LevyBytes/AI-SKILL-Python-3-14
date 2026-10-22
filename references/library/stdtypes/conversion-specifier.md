# Conversion specifier

#### Conversion specifier

By default, a replacement field expression's value is converted to a string by means of `str()`:

```python
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third}'
'1/3'

```

Where a debug specifier appears with no format specifier, the default conversion turns instead to [`repr()`](https://docs.python.org/3.14/library/functions.html#repr):

```python
>>> f'{one_third = }'
'one_third = Fraction(1, 3)'

```

The conversion can be stated outright by means of one of these specifiers:

- `!s` for `str()`

- `!r` for [`repr()`](https://docs.python.org/3.14/library/functions.html#repr)

- `!a` for [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii)

Consider this:

```python
>>> str(one_third)
'1/3'
>>> repr(one_third)
'Fraction(1, 3)'

>>> f'{one_third!s} is {one_third!r}'
'1/3 is Fraction(1, 3)'

>>> string = "¡kočka 😸!"
>>> ascii(string)
"'\\xa1ko\\u010dka \\U0001f638!'"

>>> f'{string = !a}'
"string = '\\xa1ko\\u010dka \\U0001f638!'"

```

[Subject index](INDEX.md) · [Previous](debug-specifier.md) · [Continue](format-specifier.md)
