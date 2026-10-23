# What's New In Python 3.6 / PEP 498: Formatted string literals

### New Features

### PEP 498: Formatted string literals

[**PEP 498**](https://peps.python.org/pep-0498/) brings a fresh flavor of string literals: *f-strings*, otherwise known as [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings).

A formatted string literal carries the `'f'` prefix and behaves much like the format strings handled by [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format). Inside them sit replacement fields wrapped in curly braces. Each replacement field holds an expression that gets evaluated when the program runs, then rendered through the [`format()`](https://docs.python.org/3.14/library/functions.html#format) protocol:

```python
>>> name = "Fred"
>>> f"He said his name is {name}."
'He said his name is Fred.'
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'

```

See also

[**PEP 498**](https://peps.python.org/pep-0498/): Literal String Interpolation.

PEP written and implemented by Eric V. Smith.

[Feature documentation](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings).

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-526-syntax-for-variable-annotations.md) · [Release/subject declaration](summary-release-highlights.md)
