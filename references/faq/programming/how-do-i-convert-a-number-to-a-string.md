# How do I convert a number to a string?

### How do I convert a number to a string?

As an example, turning the number `144` into the string `'144'` is done with the built-in type constructor [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str). Should you want a hexadecimal or octal form, use the built-in functions [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) or [`oct()`](https://docs.python.org/3.14/library/functions.html#oct). For elaborate formatting, consult the [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings) sections. For instance, `"{:04d}".format(144)` produces `'0144'` and `"{:.3f}".format(1.0/3.0)` produces `'0.333'`.

[Subject index](INDEX.md)
