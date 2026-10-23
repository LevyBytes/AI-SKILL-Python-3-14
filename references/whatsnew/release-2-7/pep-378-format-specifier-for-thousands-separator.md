# What’s New in Python 2.7 / PEP 378: Format Specifier for Thousands Separator - locale

### PEP 378: Format Specifier for Thousands Separator

To render program output easier to read, adding separators to large numbers can help, showing them as 18,446,744,073,709,551,616 rather than 18446744073709551616.

The completely general way to accomplish this is the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module, which supports varying separators (“,” in North America, “.” in Europe) and varying grouping sizes, yet `locale` is awkward to work with and a poor fit for multi-threaded applications where separate threads generate output for different locales.

For that reason, a straightforward comma-grouping facility was added to the mini-language behind the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method. To format a floating-point number, just place a comma between the width and the precision:

```python
>>> '{:20,.2f}'.format(18446744073709551616.0)
'18,446,744,073,709,551,616.00'

```

To format an integer, add the comma right after the width:

```python
>>> '{:20,d}'.format(18446744073709551616)
'18,446,744,073,709,551,616'

```

This facility offers no adaptability whatsoever; commas always serve as the separator and the grouping is always in groups of three digits. The comma-formatting facility lacks the generality of the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module, but it is simpler to use.

See also

[**PEP 378**](https://peps.python.org/pep-0378/) - Format Specifier for Thousands Separator

PEP written by Raymond Hettinger; implemented by Eric Smith.

[Subject index](INDEX.md) · [Previous source section](ordered-dictionaries-and-json-decoding.md) · [Next source section](pep-389-the-argparse-module-for-parsing-command-lines.md) · [Release/subject declaration](the-future-for-python-2-x.md)
