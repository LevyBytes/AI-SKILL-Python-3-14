# What’s New In Python 3.1 / PEP 378: Format Specifier for Thousands Separator - decimal

### PEP 378: Format Specifier for Thousands Separator

A mini-language drives the built-in [`format()`](https://docs.python.org/3.14/library/functions.html#format) function and the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method, and it now offers a straightforward, locale-independent route to render a number carrying a thousands separator. This gives a way to make program output friendlier, lifting both its polished look and how easily it reads:

```python
>>> format(1234567, ',d')
'1,234,567'
>>> format(1234567.89, ',.2f')
'1,234,567.89'
>>> format(12345.6 + 8901234.12j, ',f')
'12,345.600000+8,901,234.120000j'
>>> format(Decimal('1234567.89'), ',f')
'1,234,567.89'

```

Types you can use here are [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal).

There is ongoing debate over how to name other separators, such as dots, spaces, apostrophes, or underscores. Programs that care about locale ought to reach for the established *n* format specifier, which already handles thousands separators to a degree.

See also

[**PEP 378**](https://peps.python.org/pep-0378/) - Format Specifier for Thousands Separator

Raymond Hettinger authored this PEP; Eric Smith and Mark Dickinson handled the implementation.

[Subject index](INDEX.md) · [Previous source section](pep-372-ordered-dictionaries.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md)
