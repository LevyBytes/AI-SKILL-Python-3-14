# 7.1.1. Formatted String Literals

### 7.1.1. Formatted String Literals

[Formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), known for short as f-strings, allow the value of Python expressions to appear inside a string: you prefix the string with `f` or `F` and spell each expression out as `{expression}`.

After the expression you may append an optional format specifier, which hands you tighter command over the value's formatting. In the example below, pi is rounded to three digits past the decimal:

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

```

Supplying an integer following the `':'` sets a floor on how many characters wide that field becomes. It comes in handy for getting columns to align.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

```

Further modifiers let you transform the value ahead of formatting it. `'!a'` runs [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii), `'!s'` runs [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str), and `'!r'` runs [`repr()`](https://docs.python.org/3.14/library/functions.html#repr):

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

```

By way of the `=` specifier, an expression expands into the expression's own text, an equals sign, and finally the representation of what the expression evaluated to:

```python
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'

```

For fuller coverage of the `=` specifier, turn to [self-documenting expressions](https://docs.python.org/3.14/whatsnew/3.8.html#bpo-36817-whatsnew). And to look up these format specifications, the reference guide for the [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec) is where to go.

[Subject index](INDEX.md) · [Previous source section](fancier-output-formatting.md) · [Following source section](the-string-format-method.md)
