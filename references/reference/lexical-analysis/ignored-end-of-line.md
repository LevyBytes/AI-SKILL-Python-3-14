# 2.5.4.1. Ignored end of line

#### 2.5.4.1. Ignored end of line

Placing a backslash at a line's end causes the newline that follows to be discarded:

```python
>>> 'This string will not include \
... backslashes or newline characters.'
'This string will not include backslashes or newline characters.'

```

You can reach the identical outcome with triple-quoted strings, or by combining parentheses and [string literal concatenation](https://docs.python.org/3.14/reference/expressions.html#string-concatenation).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](escape-sequences.md) · [Following source section](escaped-characters.md)
