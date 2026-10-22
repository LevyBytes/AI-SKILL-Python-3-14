# 2.5.4.5. Named Unicode character

#### 2.5.4.5. Named Unicode character

A Unicode character carrying the supplied *name* is written with the `\N{*name*}` sequence:

```python
>>> '\N{LATIN CAPITAL LETTER P}'
'P'
>>> '\N{SNAKE}'
'🐍'

```

Bytes literals are not allowed to contain this sequence.

Changed in version 3.3: Support for [name aliases](https://www.unicode.org/Public/16.0.0/ucd/NameAliases.txt) has been added.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](hexadecimal-character.md) · [Following source section](hexadecimal-unicode-characters.md)
