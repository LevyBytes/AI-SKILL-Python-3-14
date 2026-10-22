# Debug specifier

#### Debug specifier

Added in version 3.8.

When a debug specifier – an equal sign (`=`) – follows the replacement field expression, the resulting f-string carries the expression's source, the equal sign, and the expression's value. This proves handy for debugging on a regular basis:

```python
>>> number = 14.3
>>> f'{number=}'
'number=14.3'

```

Whitespace ahead of, inside, and after the expression, plus whitespace following the equal sign, carries meaning — it is preserved in the outcome:

```python
>>> f'{ number  -  4  = }'
' number  -  4  = 10.3'

```

[Subject index](INDEX.md) · [Previous](formatted-string-literals-f-strings.md) · [Continue](conversion-specifier.md)
