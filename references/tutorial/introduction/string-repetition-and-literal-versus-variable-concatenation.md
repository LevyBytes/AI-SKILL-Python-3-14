# String repetition and literal versus variable concatenation

Use the `+` operator to join strings end to end (glue them together), and `*` to repeat them:

```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'

```

When a pair or more of *string literals* (those wrapped between quotes) sit side by side, they get concatenated for you automatically.

```python
>>> 'Py' 'thon'
'Python'

```

That behavior comes in especially handy for splitting up lengthy strings:

```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

```

Mind you, the trick applies to two literals alone — never to variables or to expressions:

```python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax

```

To glue together variables, or a variable next to a literal, turn to `+`:

```python
>>> prefix + 'thon'
'Python'

```

[Subject index](INDEX.md) · [Previous source section](string-quotation-escapes-raw-strings-and-multiline-literals.md) · [Following source section](string-indexing-slicing-defaults-and-slice-boundaries.md) · [Related tutorial example and explanation](string-quotation-escapes-raw-strings-and-multiline-literals.md) · [Related tutorial example and explanation](string-indexing-slicing-defaults-and-slice-boundaries.md) · [Related tutorial example and explanation](string-bounds-immutability-length-and-further-operations.md)
