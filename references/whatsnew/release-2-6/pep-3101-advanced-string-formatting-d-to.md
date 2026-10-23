# What’s New in Python 2.6 / PEP 3101: Advanced String Formatting - string

```python
>>> '{0:g}'.format(3.75)
'3.75'
>>> '{0:e}'.format(3.75)
'3.750000e+00'

```

Many presentation types exist. Refer to the 2.6 documentation for a [complete list](https://docs.python.org/3.14/library/string.html#formatstrings); the following is just a taste:

| `b` | Binary. Renders the value in base 2. |
| --- | --- |
| `c` | Character. Turns the integer into its matching Unicode character ahead of printing. |
| `d` | Decimal Integer. Renders the value in base 10. |
| `o` | Octal format. Renders the value in base 8. |
| `x` | Hex format. Writes the value in base 16, with lower-case letters standing for digits past 9. |
| `e` | Exponent notation. Shows the value in scientific form, marking the exponent with the letter ?e?. |
| `g` | General format. Here the value appears as a fixed-point figure, switching over to ?e? exponent notation once the value grows too large. |
| `n` | Number. Behaves just like ?g? for floats or ?d? for integers, save that it consults the active locale setting to add the right separator characters between digits. |
| `%` | Percentage. Scales the value by 100 and renders it in fixed (?f?) format, trailed by a percent sign. |

A class or type may supply a [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) method to govern its own formatting. That method is handed one argument, namely the format specifier:

```python
def __format__(self, format_spec):
    if isinstance(format_spec, unicode):
        return unicode(str(self))
    else:
        return str(self)

```

A [`format()`](https://docs.python.org/3.14/library/functions.html#format) builtin exists as well for formatting one lone value. It hands the supplied specifier to the type's [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) method:

```python
>>> format(75.6564, '.2f')
'75.66'

```

See also

[Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings)

The reference documentation for format fields.

[**PEP 3101**](https://peps.python.org/pep-3101/) - Advanced String Formatting

The PEP came from Talin. The implementation was carried out by Eric Smith.

[Subject index](INDEX.md) · [Previous source section](pep-3101-advanced-string-formatting-to.md) · [Next source section](pep-3105-print-as-a-function.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](pep-3101-advanced-string-formatting-to.md)
