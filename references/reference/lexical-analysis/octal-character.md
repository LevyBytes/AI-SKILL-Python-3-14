# 2.5.4.3. Octal character

#### 2.5.4.3. Octal character

A *character* whose octal (base 8) value equals *ooo* is written with the `\*ooo*` sequence:

```python
>>> '\120'
'P'

```

As many as three octal digits, ranging from 0 to 7, may be supplied.

Within a bytes literal, *character* refers to a *byte* holding that value. Within a string literal, it refers instead to a Unicode character holding that value.

Changed in version 3.11: An octal escape whose value exceeds `0o377` (255) now triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

Changed in version 3.12: An octal escape whose value exceeds `0o377` (255) now triggers a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning). A later release of Python will instead make such escapes raise a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](escaped-characters.md) · [Following source section](hexadecimal-character.md)
