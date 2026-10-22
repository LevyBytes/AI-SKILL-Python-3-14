# 2.5.4.2. Escaped characters

#### 2.5.4.2. Escaped characters

Putting a backslash inside a non-raw Python string literal requires doubling it. A lone backslash character is written with the `\\` escape sequence:

```python
>>> print('C:\\Program Files')
C:\Program Files

```

In the same way, the `\'` and `\"` sequences stand for the single-quote and double-quote characters, one each:

```python
>>> print('\' and \"')
' and "

```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](ignored-end-of-line.md) · [Following source section](octal-character.md)
