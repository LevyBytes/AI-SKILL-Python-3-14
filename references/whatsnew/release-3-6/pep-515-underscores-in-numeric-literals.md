# What's New In Python 3.6 / PEP 515: Underscores in Numeric Literals - string

### PEP 515: Underscores in Numeric Literals

[**PEP 515**](https://peps.python.org/pep-0515/) permits underscores within numeric literals so they read more clearly. To illustrate:

```python
>>> 1_000_000_000_000_000
1000000000000000
>>> 0x_FF_FF_FF_FF
4294967295

```

A single underscore may sit between digits or right after a base specifier. You cannot lead with, trail with, or chain several underscores together.

The [string formatting](https://docs.python.org/3.14/library/string.html#formatspec) mini-language likewise gains the `'_'` option, which requests an underscore as the thousands separator for floating-point presentation types and for the integer presentation type `'d'`. With the integer presentation types `'b'`, `'o'`, `'x'`, and `'X'`, an underscore lands every 4 digits:

```python
>>> '{:_}'.format(1000000)
'1_000_000'
>>> '{:_x}'.format(0xFFFFFFFF)
'ffff_ffff'

```

See also

[**PEP 515**](https://peps.python.org/pep-0515/): Underscores in Numeric Literals

PEP written by Georg Brandl and Serhiy Storchaka.

[Subject index](INDEX.md) · [Previous source section](pep-526-syntax-for-variable-annotations.md) · [Next source section](pep-525-asynchronous-generators.md) · [Release/subject declaration](summary-release-highlights.md)
