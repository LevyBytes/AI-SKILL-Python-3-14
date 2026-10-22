# 2.5.4.4. Hexadecimal character

#### 2.5.4.4. Hexadecimal character

A *character* whose hex (base 16) value equals *hh* is written with the `\x*hh*` sequence:

```python
>>> '\x50'
'P'

```

In contrast with Standard C, precisely two hex digits have to be given.

Within a bytes literal, *character* refers to a *byte* holding that value. Within a string literal, it refers instead to a Unicode character holding that value.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](octal-character.md) · [Following source section](named-unicode-character.md)
