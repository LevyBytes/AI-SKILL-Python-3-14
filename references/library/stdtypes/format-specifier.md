# Format specifier

#### Format specifier

Once the expression has been evaluated, and perhaps converted by an explicit conversion specifier, it gets formatted via the [`format()`](https://docs.python.org/3.14/library/functions.html#format) function. Should the replacement field carry a *format specifier* introduced by a colon (`:`), that specifier is handed to `format()` as the second argument. The output of `format()` then serves as the final value of the replacement field. For instance:

```python
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third:.6f}'
'0.333333'
>>> f'{one_third:_^+10}'
'___+1/3___'
>>> f'{one_third!r:_^20}'
'___Fraction(1, 3)___'
>>> f'{one_third = :~>10}~'
'one_third = ~~~~~~~1/3~'
```

[Subject index](INDEX.md) · [Previous](conversion-specifier.md) · [Continue](template-string-literals-t-strings.md)
