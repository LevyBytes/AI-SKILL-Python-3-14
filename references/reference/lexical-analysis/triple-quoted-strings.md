# 2.5.1. Triple-quoted strings

### 2.5.1. Triple-quoted strings

Matching groups of three single or double quotes can also wrap strings. The common term for these is *triple-quoted strings*:

```python
"""This is a triple-quoted string."""

```

Inside triple-quoted literals, unescaped quotes are permitted (and kept), the exception being that three unescaped quotes in a row close the literal when they match the kind (`'` or `"`) that opened it:

```python
"""This string has "quotes" inside."""

```

Unescaped newlines are permitted and kept as well:

```python
'''This triple-quoted string
continues on the next line.'''

```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](string-and-bytes-literals.md) · [Following source section](string-prefixes.md)
